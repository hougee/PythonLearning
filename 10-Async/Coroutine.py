#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'此模块功能：最简单的协程例子'


__author__ = 'HouBin'

#生成器函数
def consumer():
    rTemp = ''
    while True:
        #生成器通过yield获取消息，处理完毕后，通过yield把结果传回
        n = yield rTemp
        if not n:
            return
        print('[CONSUMER] Consuming %s...' % n)
        rTemp = '200 OK'

def produce(cTemp):
    #启动生成器
    cTemp.send(None)
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
        r = cTemp.send(n)
        print('[PRODUCER] Consumer return: %s' % r)
    #关闭生成器
    cTemp.close()

c = consumer()
produce(c)
