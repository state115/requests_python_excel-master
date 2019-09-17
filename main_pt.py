# -*- coding: utf_8 -*-
# 文件名称：main_pt.py
# locust基础性能测试模板
from locust import HttpLocust, TaskSet, task
import subprocess
import json
# 性能测试任务类 TaskSet.
class UserBehavior(TaskSet):
    # 开始
    def on_start(self):
        pass
    # 任务
    @task(1)
    def getTagVals(self):
        u"""
        request_url：请求路径
        request_params：请求头参数
        request_json：请求json参数
        """
        request_url = "http://192.168.1.192/appprogram/fiction-chapter/book-reading-add"
        request_params = {
            "device_id": "F47E8319-A653-4F8D-ABC7-08680923CBC3",
            "token": "e201754e074e5b439d9683919f6542fa",
            "nid": "7714",
            "chapnum": "2"
        }
        request_json = {
            "tagKey": 25
        }
        response = self.client.post(
            url=request_url,
            params=request_params,
        )
        if response.status_code != 200:
            print (u"返回异常")
            print (u"请求返回状态码:", response.status_code)
        elif response.status_code == 200:
            print (u"返回正常")
        # 这里可以编写自己需要校验的返回内容
        # content = json.loads(response.content)["content"]
        # if content["tagKey"] == 25:
        #     print u"校验成功"
        #     print json.dumps(content, encoding="UTF-8", ensure_ascii=False)
# 性能测试配置
class MobileUserLocust(HttpLocust):
    u"""
    min_wait ：用户执行任务之间等待时间的下界，单位：毫秒。
    max_wait ：用户执行任务之间等待时间的上界，单位：毫秒。
    """
    # weight = 3
    task_set = UserBehavior
    host = "http://192.168.1.192"
    min_wait = 3000
    max_wait = 6000
if __name__ == "__main__":
    subprocess.Popen("locust -f main_pt.py", shell=True)