#!/usr/bin/env python 
# coding:utf-8
# import requests
# # requestsparam1={ "id": "3","device_id": "W1CItOrPwxgDABXkhg4huB7e","token": ""}
# r1=requests.post('http://api.zhuishubao.com/appprogram/static/user-faq')
# print(r1.text)
# print(r1.status_code)

import requests
import json
d={  "tag_id_gather": "30,31,34,35,36",
         "page": "1",
         "pageSize": "20",
         "token": "db60511d2ba61d627b0703a1f70f3f08",
         "device_id": "XQ2KXPbIcioDAIBkCYwO MhZ"}
r1=requests.post('http://api.zhuishubao.com/appprogram/articles/article-list',data=d )
print(r1.text)
print(r1.status_code)