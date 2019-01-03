#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
此模块功能：filter模块（寻找素数）
详细说明：
见注释
'''

__author__ = 'HouBin'

#构造一个从3开始的奇数序列（需要注意这是一个生成器，且为无限序列）
def _odd_iter():
    oddNum = 1
    while True:
        oddNum = oddNum + 2
        yield oddNum

#定义一个筛选函数（注意返回的是一个匿名函数）
def _not_divisible(nTemp):
    return lambda x: x % nTemp > 0

#定义一个生成器不断返回下一个素数
def primes():
    #首先生成第一个数2
    yield 2
    #生成初始序列
    it = _odd_iter()
    while True:
        #从待定序列中依次取出第一个数
        n = next(it)
        #此时第一个数肯定为素数
        yield n
        #用第一个数筛选原序列（注意_not_divisible(n)仍然是 一个函数）
        it = filter(_not_divisible(n), it)

if __name__ == '__main__':
    for prime in primes():
        if prime < 1000:
            print(prime)
        else:
            break
