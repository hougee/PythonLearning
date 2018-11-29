#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
此模块功能：itertools提供用于操作迭代对象的函数'''

__author__ = 'HouBin'

import itertools

#count()会创建一个无限计数迭代器
natuals = itertools.count(1)
for n in natuals:
    print(n)
    if n >= 100:
        break

#cycle()会把传入的一个序列无限重复
cs = itertools.cycle('ABC') # 注意字符串也是序列的一种
t = 10
for c in cs:
    print(c)
    t = t - 1
    if t == 0:
        break

#repeat()负责把一个元素无限重复下去，如果提供第二个参数就可以限定重复次数
ns = itertools.repeat('dd', 3)
for n in ns:
    print(n)

#takewhile()等函数根据条件判断从无限序列截取出一个有限的序列
natuals = itertools.count(1)
ns = itertools.takewhile(lambda x: x <= 10, natuals)
print(list(ns))

#chain()可以把一组迭代对象串联起来，形成一个更大的迭代器
for c in itertools.chain('ABC', 'XYZ'):
    print(c)

#groupby()把迭代器中相邻的重复元素挑出来放在一起
for key, group in itertools.groupby('AAABBBCCAAA'):
    print(key, list(group))
'''
实际上挑选规则是通过函数完成的，只要作用于函数的两个元素返回的值相
等，这两个元素就被认为是在一组的，而函数返回值作为组的key。如果我
们要忽略大小写分组，就可以让元素'A'和'a'都返回相同的key
'''
for key, group in itertools.groupby('AaaBBbcCAAa', lambda c: c.upper()):
    print(key, list(group))
