#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
功能说明：读写文件
'''

__author__ = 'HouBin'

from datetime import datetime

#第一种读写文件方法（不推荐）
try:
    f = open('test.txt', 'w') 
    f.write('今天是 ') #或者f.read()
    f.write(datetime.now().strftime('%Y-%m-%d'))
finally:
    if f:
        f.close() #必须把文件关闭
'''
注意：
（1）标示符'r'表示读取文本文件，标示符'rb'表示读取二进制文件，
标识符'w'表示写文本文件，标识符'wb'表示写二进制文件，
标识符'a'表示以追加（append）模式写入；
（2）在读文件时，如果文件不存在，open()函数就会抛出一个IOError的错误；
（3）read()一次性读取文件的全部内容，read(size)每次最多
读取size个字节的内容，readline()每次读取一行内容，
readlines()一次读取所有内容并按行返回list列表
(line.strip()可以把末尾的'\n'删掉);
'''
#第二种读写文件方法（推荐）
with open('test.txt', 'a') as f:
    f.write('今天是 ')
    f.write(datetime.now().strftime('%Y-%m-%d'))

with open('test.txt', 'r') as f:
    s = f.read()
    print('open for read...')
    print(s)

with open('test.txt', 'rb') as f:
    s = f.read()
    print('open as binary for read...')
    print(s)
