#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'此模块功能：通过串口读取六轴陀螺仪数据（适配型号为维特智能WT61C-TTL）示例'

__author__ = 'HouBin'

#pyserial安装：sudo apt-get install python-serial 或 pip3 install pyserial

import serial
import time
import threading
import types

STRGLO="" #读取的数据
BOOL=True  #读取标志位

#端口，GNU/Linux上的/dev/ttyUSB0等或Windows上的COM3等
#portx="/dev/ttyAMA0"
portx="COM3"
#波特率，标准值之一：50,75,110,134,150,200,300,600,1200,1800,2400,4800,9600,19200,38400,57600,115200
bps=115200
#超时设置,None：永远等待操作，0为立即返回请求结果，其他值为等待超时时间(单位为秒）
timex=None

#读数代码本体实现
def ReadData(ser):
    global STRGLO,BOOL
    # 循环接收数据，此为死循环，可用线程实现
    while BOOL:
        if ser.in_waiting:
            STRGLO = ser.read(ser.in_waiting)
            #print(STRGLO)
        #清空接收缓冲区
        ser.flushInput()
        #必要的软件延时
        time.sleep(0.06)
         
#打开串口
def DOpenPort(portx,bps,timeout):
    ret=False
    try:
        # 打开串口，并得到串口对象
        ser = serial.Serial(portx, bps, timeout=timeout)
        #判断是否打开成功
        if(ser.is_open):
            ret=True
            threading.Thread(target=ReadData, args=(ser,)).start()
    except Exception as e:
        print("---异常---：", e)
    return ser,ret

#关闭串口
def DColsePort(ser):
    global BOOL
    BOOL=False
    ser.close()
    
#读数据
def DReadPort():
    global STRGLO
    strRead=STRGLO
    STRGLO=""#清空当次读取
    return strRead

#负数转换函数
def NegativeTransform(number):
    if number>=0x8000:
        number=number-0xffff
    return number

if __name__ == '__main__':
    ser,ret=DOpenPort(portx,bps,timex)
    if(ret==True):#判断串口是否成功打开
        while True:
            #读取一次串口数据
            strRead=DReadPort()
            #判断数据是否为字节型，且长度超过66个字节
            if(type(strRead) ==type(b" ") and len(strRead)>66):
                #成功获取数据标志位
                getDataFlag=False
                #初始化加速度、角速度、角度
                a=[0,0,0]
                w=[0,0,0]
                R=[0,0,0]
                for index in range(33):
                    #截取一次完整数据
                    if(strRead[index]==0x55 and strRead[index+1]==0x51 and strRead[index+11]==0x55 and strRead[index+12]==0x52 and strRead[index+22]==0x55 and strRead[index+23]==0x53):
                        #计算加速度
                        a[0]=NegativeTransform((strRead[index+3]<<8)|strRead[index+2])/32768*16*9.8
                        a[1]=NegativeTransform((strRead[index+5]<<8)|strRead[index+4])/32768*16*9.8
                        a[2]=NegativeTransform((strRead[index+7]<<8)|strRead[index+6])/32768*16*9.8
                        #计算角速度
                        w[0]=NegativeTransform((strRead[index+14]<<8)|strRead[index+13])/32768*2000
                        w[1]=NegativeTransform((strRead[index+16]<<8)|strRead[index+15])/32768*2000
                        w[2]=NegativeTransform((strRead[index+18]<<8)|strRead[index+17])/32768*2000
                        #计算角度
                        R[0]=NegativeTransform((strRead[index+25]<<8)|strRead[index+24])/32768*180
                        R[1]=NegativeTransform((strRead[index+27]<<8)|strRead[index+26])/32768*180
                        R[2]=NegativeTransform((strRead[index+29]<<8)|strRead[index+28])/32768*180
                        #成功获取数据后标志位置1
                        getDataFlag=True
                        break
                if(getDataFlag):
                    print("*************")
                    print("加速度：",a)
                    print("角速度：",w)
                    print("角度：",R)
            time.sleep(1)
        #DReadPort() #读串口数据
        #DColsePort(ser)  #关闭串口
        
