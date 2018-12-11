#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'此模块功能：TCP网络示例服务器程序'

__author__ = 'HouBin'

import socket
import threading
from time import sleep
def response(sock, addr):
    print("客户端%s:%d已经连接到服务器。"%(addr[0],addr[1]))
    t=input("请输入需要向客户端发送的数据：")
    sock.send(t.encode('utf8'))
    while True:
        t=sock.recv(1024).decode('utf8')  #函数的核心语句就一条接收方法
        if t == "exit":
            true=False
        elif t=="你好，服务器！":
            print("-----------------------------------------------------------")
            print("收到客户端数据："+t+"，")
            print("给客户端发送数据：客户端，你吃饭了吗？")
            sock.send("客户端，你吃饭了吗？".encode('utf8'))
        elif t=="我吃过了，你呢，服务器？":
            print("-----------------------------------------------------------")
            print("收到客户端数据："+t+"，")
            print("给客户端发送数据：我也吃过了，吃的很饱。")
            sock.send("我也吃过了，吃的很饱。".encode('utf8'))
        else:
            print("-----------------------------------------------------------")
            print("收到客户端数据："+t+"，")
            print("无返回数据。")
    #sock.send(html.encode('utf8'))
    sock.close()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("127.0.0.1",8888))
s.listen(50)
print("启动服务器，正在等待连接……")
while 1:
    sleep(0.1) 
    sock,addr = s.accept() 
    t = threading.Thread(target=response, args=(sock,addr))
    t.start()
