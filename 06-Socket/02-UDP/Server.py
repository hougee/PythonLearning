#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'此模块功能：UDP网络示例服务器程序'

__author__ = 'HouBin'

import socket
import time

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 绑定端口:
s.bind(('localhost', 9999))
print('服务器绑定UDP端口：9999...')
while True:
    #接收数据
    data, addr = s.recvfrom(1024)
    print("-----------------------------------------------------------")
    print('收到来自%s:%s的消息：' % addr)
    print(data.decode('utf-8'))
    if data.decode('utf-8')=="你好，服务器！":
        #发送数据
        s.sendto(("你好，客户端%s:%s！" % addr).encode('utf-8'), addr)
    elif data.decode('utf-8')=="服务器，你吃饭了吗？":
        #向客户端2发送数据
        s.sendto("我吃过了，客户端2，你吃了吗？".encode('utf-8') , addr)
        print("向客户端2发送数据：我吃过了，客户端2，你吃了吗？")
    elif data.decode('utf-8')=="我吃过了。":
        time.sleep(5)
        #向客户端1发送数据
        s.sendto("散会！".encode('utf-8') , ('127.0.0.1', 6666))
        print("向客户端1发送数据：散会！")
        #向客户端2发送数据
        s.sendto("散会！".encode('utf-8') , ('127.0.0.1', 8888))
        print("向客户端2发送数据：散会！")
