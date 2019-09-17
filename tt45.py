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
            'book_id': data['book_id'],
        }

        self.client.post("http://192.168.1.192/appprogram/fiction/v2/book-detail", data=payload)
        self.locust.user_data_queue.put_nowait(data)


class MobileUserLocust(HttpLocust):
    host="http://192.168.1.192"
    task_set = UserBehavior

    user_data_queue = queue.Queue()
    for index in range(50):
        data = {
            "device_id": "86945704162108%d" % index,
            "book_id": "100%d" % index,
        }
        user_data_queue.put_nowait(data)

    min_wait = 1000
    max_wait = 3000

if __name__ == "__main__":
    subprocess.Popen("locust -f tt45.py", shell=True)