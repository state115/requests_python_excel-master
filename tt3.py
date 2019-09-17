#!/usr/bin/env python 
# coding:utf-8
import json
import os
from random import randint
import subprocess
from locust import HttpLocust, TaskSet, task


# Read json file
json_file = os.path.join(os.path.dirname(__file__), 'payloads.json')

class UserBehavior(TaskSet):
    def on_start(self):
        self.index = 0

    def __init__(self, parent):
        super(UserBehavior, self).__init__(parent)
        with open(json_file) as file:
            self.payloads = json.load(file, 'utf-8')
        self.length = len(self.payloads) - 1

    @task(1)
    def post_random_payload(self):
        p = self.payloads[randint(0, self.length)]
        print(p)
        response = self.client.post('http://192.168.1.192/appprogram/fiction-chapter/chapter-content', json={'device_id': p.get('device_id'), 'token': p.get('token'),'nid': p.get('nid'),'chapnum': p.get('chapnum')})
        # self.client.post('/', json={'device_id': p.get('device_id'), 'token': p.get('token'),'nid': p.get('nid'),'chapnum': p.get('chapnum')})

        if response.status_code != 200:
            print(u"返回异常")
            print(u"请求返回状态码:", response.status_code)
        elif response.status_code == 200:
            print(u"返回正常")


# class MyLocust(HttpLocust):
#     task_set = UserBehavior
#     host = "http://192.168.1.192"
#     min_wait = 0
#     max_wait = 0
#
#
# if __name__ == "__main__":
#     subprocess.Popen("locust -f tt3.py", shell=True)