#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
此模块功能：filter模块（1.删掉偶数，只保留奇数；2.把一个序列中的空字符串删掉）
详细说明：
filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素
'''


__author__ = 'HouBin'

def is_odd(n):
    return n % 2 == 1

L = range(100)

print(list(filter(is_odd, L)))

def not_empty(s):
    return s and s.strip()

print(list(filter(not_empty, ['A', '', 'B', None, 'C', '  '])))
