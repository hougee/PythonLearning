#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'此模块功能：TCP网络示例客户端程序'

__author__ = 'HouBin'

import socket
import threading
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(("127.0.0.1",8884))
print("启动客户端，正在连接服务器>>>")
s.connect(("127.0.0.1",8888))
print("已连接到服务器。")
true=True
def rec(s):
    global true
    while true:
        t=s.recv(1024).decode("utf8")  #客户端也同理
        if t == "exit":
            print("-----------------------------------------------------------")
            print("收到服务器数据："+t+"，")
            print("断开与服务器连接。")
            true=False
        elif t=="你好，客户端！":
            print("-----------------------------------------------------------")
            print("收到服务器数据："+t+"，")
            print("给服务器发送数据：你好，服务器！")
            s.send("你好，服务器！".encode('utf8'))
        elif t=="客户端，你吃饭了吗？":
            print("-----------------------------------------------------------")
            print("收到服务器数据："+t+"，")
            print("给服务器发送数据：我吃过了，你呢，服务器？")
            s.send("我吃过了，你呢，服务器？".encode('utf8'))
        else:
            print("-----------------------------------------------------------")
            print("收到服务器数据："+t+"，")
            print("无返回数据。")
trd=threading.Thread(target=rec,args=(s,))
trd.start()
while true:
    #t=input("t=")
    #s.send(t.encode('utf8'))
    #if t == "exit":
    #    true=False
    pass
s.close()
