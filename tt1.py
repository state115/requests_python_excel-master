#!/usr/bin/env python
# coding:utf-8
import requests
import json # 使用到JSON中的方法，需要提前导入

# url = "http://api.zhuishubao.com/appprogram/articles/article-list"
# datas = {
#          "tag_id_gather": "30,31,34,35,36",
#          "page": "1",
#          "pageSize": "20",
#          "token": "db60511d2ba61d627b0703a1f70f3f08",
#          "device_id": "XQ2KXPbIcioDAIBkCYwO MhZ"
#         }  # 字典格式，方便添加
# headers = {"Content-Type":"application/json"} # 严格来说，我们需要在请求头里声明我们发送的格式
# res = requests.post(url=url, data=datas) #  将字典格式的data变量转换为合法的JSON字符串传给post的data参数
# print(res.text)
#
# print(res.status_code)


class Student:
    def __init__(self):  # 两者之间的区别
        self.name = None
        self.score = None

    # def __init__(self, name, score):
    #     self.name = name
    #     self.score = score

    def print_score(self):
        print("%s score is %s" % (self.name, self.score))

    def get_grade(self):
        if self.score >= 80:
            return "A"
        elif self.score >= 70:
            return "B"
        else:
            return "C"


# student = Student("sansan", 90)
student = Student()
student.name = "sansan"
student.score = 90

# susan = Student("sunny", 78)
susan = Student()
susan.name = "susan"
susan.score = 8

student.print_score()
susan.print_score()
print(susan.get_grade())

print(student.get_grade())
