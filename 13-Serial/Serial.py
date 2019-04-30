#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'此模块功能：串口通信示例'

__author__ = 'HouBin'

#pyserial安装：sudo apt-get install python-serial 或 pip3 install pyserial

import serial
import serial.tools.list_ports
import time

#获取串口列表
port_list=list(serial.tools.list_ports.comports())
print(port_list)
if len(port_list) == 0:
    
   print('无可用串口')
else:
    for i in range(0,len(port_list)):
        print(port_list[i])

#端口，GNU/Linux上的/dev/ttyUSB0等或Windows上的COM3等
#portx="/dev/ttyAMA0"
portx="COM3"
#波特率，标准值之一：50,75,110,134,150,200,300,600,1200,1800,2400,4800,9600,19200,38400,57600,115200
bps=115200
#超时设置,None：永远等待操作，0为立即返回请求结果，其他值为等待超时时间(单位为秒）
timex=None
#打开串口，获取对象
ser=serial.Serial(portx,bps,timeout=timex)
#串口详情参数
print("串口详情参数：", ser)
#获取到当前打开的串口名
print(ser.port)
#获取波特率
print(ser.baudrate)
#写数据
result=ser.write("我是串口发送的数据".encode("gbk"))
print("写总字节数:",result)
#十六进制的发送
result=ser.write(chr(0x06).encode("utf-8"))
print("写总字节数:",result)
#十六进制的读取
#print(ser.read().hex())#读一个字节
#读一个字节
#print(ser.read())
#读十个字节
#print(ser.read(10).decode("gbk"))
#读一行
#print(ser.readline().decode("gbk"))
#读取多行，返回列表，必须匹配超时（timeout)使用
#print(ser.readlines())
#获取输入缓冲区的剩余字节数
#print(ser.in_waiting)
#获取输出缓冲区的字节数
#print(ser.out_waiting)
#关闭串口
#ser.close()
def main():
    while True:
        #获得接收缓冲区字符
        count = ser.inWaiting()
        if count != 0:
            #读取内容并回显
            recv = ser.read(count)
            ser.write(recv)
        #清空接收缓冲区
        ser.flushInput()
        #必要的软件延时
        time.sleep(0.1)
    
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        if ser != None:
            ser.close()
