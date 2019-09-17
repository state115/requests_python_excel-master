# -*- coding: utf_8 -*-
# 文件名称：main_pt.py
# locust基础性能测试模板

from locust import HttpLocust, TaskSet, task
import subprocess
import queue

class UserBehavior(TaskSet):

    @task

    def getTagVals(self):

        try:
            data = self.locust.user_data_queue.get()

        except queue.Empty:
            print ("no data exist")
            exit(0)

        payload = {
            'device_id': data['device_id'],
            'token': data['token'],
            'nid': data['nid'],
            'chapnum': data['chapnum'],
        }


        self.client.post("http://192.168.1.192/appprogram/fiction-chapter/chapter-content",data=payload)
        self.locust.user_data_queue.put_nowait(data)

class MobileUserLocust(HttpLocust):
    host="http://192.168.1.192"
    task_set = UserBehavior

    user_data_queue = queue.Queue()
    for index in range(50):
        data = {
         "device_id": "test%04d" % index,
         "token": "e201754e074e5b439d9683919f6542fa",
         "nid": "8373",
         "chapnum": "1%d" % index,
        }
        user_data_queue.put_nowait(data)

    min_wait = 1000
    max_wait = 3000

if __name__ == "__main__":
    subprocess.Popen("locust -f tt4.py", shell=True)