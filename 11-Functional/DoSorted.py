#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
此模块功能：sorted模块
'''


__author__ = 'HouBin'

from operator import itemgetter

L = ['bob', 'about', 'Zoo', 'Credit']
#sorted()函数可以对list进行排序
print(sorted(L))
#sorted()函数也是一个高阶函数，可以接收一个key函数来实现自定义的排序
print(sorted(L, key=str.lower))

students = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

print(sorted(students, key=itemgetter(0)))
print(sorted(students, key=lambda t: t[1]))
#通过设置第三个参数reverse=True，可以进行反向排序
print(sorted(students, key=itemgetter(1), reverse=True))
