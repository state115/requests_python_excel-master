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
            print("no data exist")
            exit(0)

        payload = {
            'device_id': data['device_id'],
            'cat_id': data['cat_id'],
        }

        self.client.post("/appprogram/fiction/book-channel", data=payload)
        self.locust.user_data_queue.put_nowait(data)


class MobileUserLocust(HttpLocust):
    host="http://192.168.1.192"
    task_set = UserBehavior

    user_data_queue = queue.Queue()
    for index in range(50):
        data = {
            "device_id": "34945704162108%d" % index,
            "cat_id": "23" ,
        }
        user_data_queue.put_nowait(data)

    min_wait = 1000
    max_wait = 3000

if __name__ == "__main__":
    subprocess.Popen("locust -f tt46.py", shell=True)