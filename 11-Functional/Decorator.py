#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
此模块功能：装饰器
'''


__author__ = 'HouBin'

import functools

#定义一个装饰器（装饰器实质上就是：接受一个函数作为参数，并返回一个函数）
def log(func):
    #防止装饰器改变了被装饰函数的默认属性（如被装饰函数的函数名等）
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('调用函数 %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper
#定义一个带装饰器的函数
@log
def now():
    print('2015-3-25')

#定义一个带参数的装饰器
def logger(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator
#定义一个带装饰器的函数，且装饰器本身可以传入参数
@logger('调试函数')
def today():
    print('2015-3-25')

#定义一个带参数的测量函数运行时间的装饰器
import time
def timer(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args,**kw):
            start=time.time()
            func(*args,**kw)
            stop=time.time()
            print("%s（%s）的运行时间为：%f 秒"%(text,func.__name__,stop-start))
        return wrapper
    return decorator
@timer("测试函数")
def test():
    time.sleep(2)
    print("我是测试函数运行时间的函数！")
    
if __name__=="__main__":
    now()
    print(now.__name__)
    today()
    print(today.__name__)
    test()
