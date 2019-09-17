#!/usr/bin/env python 
# coding:utf-8
import requests
import json # 使用到JSON中的方法，需要提前导入
url = "http://log.ireader.com/log-agent/rlog/"
# data={
#    "token": "13324r423423ede23"
# }
# r1=requests.post('http://api.zhuishubao.com/appprogram/V2/user-behavior/video-watch-add',params=data)
# print(r1.text)
# print(r1.status_code)


data={
   "data2": {"event_id":"ireader.user.click","params":{"cli_res_type":"confirm","page_key":"11529308","page_type":"reading","block_name":"加入书架弹窗","block_type":"window"}},
   "sign" :"8f7bb537bd8d13cac9701ecd1dd20ee9",
  "topic" :	"android.ireader.realtime.event",
"sign_type" :	"MD5",
"logAdapter" :	"A1",
"public_params" : {"user_id":"i2048289707","device_id":"XRxsLGEdAVsDABVQ6la5jbV3","network":"3","channel_id":"124012","app_platform":"501656","ts":"1562147782557","model":"xiaomi Redmi 6","version_code":"17101556","ip":"119.137.53.133","imei":"867303033996430","os_ver":"8.1.0","inner_version":"17101556","app_version":"17101556","os_type":"android"}

}

headers = {"Content-Type":"application/json"} # 严格来说，我们需要在请求头里声明我们发送的格式

res = requests.post(url=url, data=json.dumps(data), headers=headers)
print(res.text)
print(res.status_code)

# import requests
# import json # 使用到JSON中的方法，需要提前导入
#
# url = "http://httpbin.org/post"
# data = {
#         "name": "hanzhichao",
#         "age": 18
#         }  # 字典格式，方便添加
# headers = {"Content-Type":"application/json"} # 严格来说，我们需要在请求头里声明我们发送的格式
# res = requests.post(url=url, data=json.dumps(data), headers=headers) #  将字典格式的data变量转换为合法的JSON字符串传给post的data参数
print(res.text)
