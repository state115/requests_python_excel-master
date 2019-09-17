# import requests
# import json
# d = {
#      "page": "1",
#      "pageSize": "20",
#      "cat_id": "18",
#      "type": "like",
#     "device_id": "860604044727590",
#     "version": "2"
# }
#
# r1=requests.post('http://apiprd.zhuishubao.com/appprogram/fiction/v2/book-screen-recommend',data=d )
# print(r1.text)
# print(r1.status_code)
# import requests
# import json
# d = {
#      "cat_id": "1",
#      "device_id": "20",
#      "version": "2"
# }
#
# r1=requests.post('http://apiprd.zhuishubao.com/appprogram/fiction/book-mall-carousel',data=d )
# print(r1.text)
# print(r1.status_code)

import requests

# d = {
#      "id": "7151",
#      "device_id": "860604044727590",
#      "version": "2"
# }
#
# r1=requests.post('http://apiprd.zhuishubao.com/appprogram/fiction-chapter/chapter-list',data=d )
# print(r1.text)
# print(r1.status_code)

# d = {
#      "nid": "7152",
#      "page": "1",
#      "pageSize": "20",
#      "device_id": "860604044727590",
#      "version": "2"
# }
#
# r1=requests.post('http://apiprd.zhuishubao.com/appprogram/user-favorite-book/list2',data=d )
# print(r1.text)
# print(r1.status_code)


# d = {
#      "id": "7152",
#      "token": "",
#      "device_id": "860604044727590",
#      "version": "2"
# }
#
# r1=requests.post('http://apiprd.zhuishubao.com/appprogram/fiction/book-detail',data=d )
# print(r1.text)
# print(r1.status_code)


# d = {
#      "read_action": "start",
#      "nid": "7152",
#      "chapnum": "5",
#      "token": "",
#      "device_id": "860604044727590",
#      "version": "2"
# }
#
# r1=requests.post('http://apiprd.zhuishubao.com/appprogram/user-read/duration-append',data=d )
# print(r1.text)
# print(r1.status_code)


# d = {
#      "nid": "7152",
#      "chapnum": "5",
#      "token": "",
#      "device_id": "860604044727590",
#      "version": "2"
# }
#
# r1=requests.post('http://apiprd.zhuishubao.com/appprogram/fiction-chapter/book-reading-add',data=d )
# print(r1.text)
# print(r1.status_code)



# d = {
#      "nid": "7152",
#      "chapnum": "5",
#      "token": "",
#      "device_id": "860604044727590",
#      "version": "2",
#      "channel": "baidu",
#      "phoneType": "1"
# }
#
# r1=requests.post('http://192.168.1.192/appprogram/fiction-chapter/book-reading-add',data=d )
# print(r1.text)
# print(r1.status_code)

# d = {
#      "nid": "7152",
#      "token": "",
#      "device_id": "860604044727590",
#      "version": "2",
#      "channel": "baidu",
#      "phoneType": "1"
# }
#
# r1=requests.post('http://192.168.1.192/appprogram/user-favorite-book/add',data=d )
# print(r1.text)
# print(r1.status_code)

# d = {
#      "nid": "7152",
#     "chapnum": "5",
#      "token": "",
#      "device_id": "860604044727590",
#      "version": "2",
#      "channel": "baidu",
#      "phoneType": "1",
#      "duration": "3600"
# }
#
# r1=requests.post('http://192.168.1.192/appprogram/user-read/duration-report',data=d )
# print(r1.text)
# print(r1.status_code)

d = {
     "device_id": "860604044727590",
     "cat_id": "17"
}

r1=requests.post('http://192.168.1.192/appprogram/fiction/book-channel-store',data=d )
print(r1.text)
print(r1.status_code)