#-*- coding:utf-8 -*-
import commands
import re
def deviceinfo():
    global deviceName,platformVersion,udid
    deviceName,platformVersion,udid = 0,0,0
    deviceUdid = commands.getoutput('system_profiler SPUSBDataType | grep "Serial Number:.*" | sed s#".*Serial Number: "##')
    deviceNumlist = deviceUdid.split('\n')
    alldevice = commands.getoutput('instruments -s devices')
    #print len(deviceUdid)
    if len(deviceUdid)==0:
        print ("无设备连接，请连接设备")
    elif len(deviceUdid)==40:
        print ("连接一台设备，开始测试")
        name =re.findall(r'(?<=\n).*'+deviceUdid,alldevice)[0]
        deviceName =re.findall(r'.*(?=\(9)',name)[0]
        platformVersion =re.findall(r'(?<=\().*(?=\))',name)[0]
        udid = re.findall('(?<=\[).*',name)[0]

    elif  len(deviceUdid)==81:
        print ("连接2台设备，请选择测试设备，\n选择"+deviceNumlist[0]+"请输入0，\n选择",deviceNumlist[1],"请输入1")
        num =input()
        name =re.findall(r'(?<=\n).*'+deviceNumlist[num],alldevice)[0]
        print (name)
        deviceName =re.findall(r'.*(?=\(9)',name)[0]
        platformVersion =re.findall(r'(?<=\().*(?=\))',name)[0]
        udid = re.findall('(?<=\[).*',name)[0]
    else:
        print ("最多连接两台设备")

deviceinfo()