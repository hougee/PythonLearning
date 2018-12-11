#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'此模块功能：UDP网络示例客户端2程序'

__author__ = 'HouBin'

import socket
import time

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('localhost', 8888))
print('客户端2绑定UDP端口：8888...')
print("向服务器发送数据：你好，服务器！")
# 发送数据
s.sendto("你好，服务器！".encode('utf-8') , ('localhost', 9999))
#监听接收
flag=True
while flag:
    data, addr = s.recvfrom(1024)
    print("-----------------------------------------------------------")
    print('收到来自%s:%s的消息：' % addr)
    print(data.decode('utf-8'))
    if data.decode('utf-8')=="你好，客户端127.0.0.1:8888！":
        #向服务器发送数据
        s.sendto("服务器，你吃饭了吗？".encode('utf-8') ,addr)
        print("向服务器发送数据：服务器，你吃饭了吗？")
        #向客户端1发送数据
        s.sendto("客户端1，你吃饭了吗？".encode('utf-8') , ('127.0.0.1', 6666))
        print("向客户端1发送数据：客户端1，你吃饭了吗？")
    elif data.decode('utf-8')=="我吃过了，客户端2，你吃了吗？":
        #向客户端1发送数据
        s.sendto("我吃过了。".encode('utf-8') ,addr)
        print("向客户端1发送数据：我吃过了。")
    elif data.decode('utf-8')=="散会！":
        #服务器发送数据
        s.sendto("客户端2下线，再见！".encode('utf-8')  , addr)
        print("向服务器发送数据：客户端2下线，再见！")
        flag=False
s.close()
