

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
# print(res.text)

import requests
import json # 使用到JSON中的方法，需要提前导入

url = "http://hrppq.info/login.shtml"
data = {
         "AJAXREQUEST": "LGForm: j_id3",
            "LGForm": "LGForm",
            "txtName": "admin118",
            "txtPsw": "huawei115",
            "LGForm: waitingInfoPanelOpenedState": "",
            "javax.faces.ViewState": "j_id2",
            "un": "admin118",
            "pwd": "huawei115",
            "LGForm: j_id4": " LGForm: j_id4"
        }  # 字典格式，方便添加
headers = {"Content-Type":"application/json"} # 严格来说，我们需要在请求头里声明我们发送的格式
res = requests.post(url=url, data=json.dumps(data), headers=headers) #  将字典格式的data变量转换为合法的JSON字符串传给post的data参数
print(res.text)

print(res.status_code)
