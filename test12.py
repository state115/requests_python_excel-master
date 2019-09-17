#!/usr/bin/env python 
# coding:utf-8
import requests
data={
   "device_id": "13324r423423ede23","nid":"19"
}
r1=requests.post('http://apitest2.zhuishubao.com/appprogram/user-favorite-book/add',params=data)
print(r1.text)
print(r1.status_code)