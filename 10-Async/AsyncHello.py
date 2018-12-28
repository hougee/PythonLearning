#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'此模块功能：利用标准库asyncio实现异步IO'


__author__ = 'HouBin'

import threading
import asyncio

#通过装饰器把一个生成器标记为协程类型
@asyncio.coroutine
def hello(name):
    print('Hello, %s! (%s)' % (name, threading.currentThread()))
    yield from asyncio.sleep(1)
    print('See you again, %s! (%s)' % (name, threading.currentThread()))

loop = asyncio.get_event_loop()
tasks = [hello("Zhangsan"), hello("Lisi"), hello("Wangwu")]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()
