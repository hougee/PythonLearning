#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
功能说明：操作文件和目录
'''

__author__ = 'HouBin'

from datetime import datetime
import os

print("获取操作系统类型（‘posix’：Linux、Unix或Mac OS X，‘nt’：Windows系统）:")
print(os.name)

#print("获取系统详细信息，Windows系统下不可用")
#print(os.uname())

print("获取系统环境变量:")
print(os.environ)

print("获取某个环境变量的值:")
print(os.environ.get('PATH'))

print("查看当前目录的绝对路径:")
pwd = os.path.abspath('.')
print(pwd)

print("在某个目录下创建一个新目录:")
testDir=os.path.join(pwd, 'testdir')
print(testDir)
os.mkdir(testDir) #然后创建一个目录
print("新目录已创建")
os.rmdir(testDir) #删掉一个目录
print("新目录已删除")

print("把一个路径拆分为两部分:")
print(os.path.split('/Users/michael/testdir/file.txt')) #把一个路径拆分为两部分，后一部分总是最后级别的目录或文件名：('/Users/michael/testdir', 'file.txt')

print("获得文件扩展名：")
print(os.path.splitext('/path/to/file.txt')) #获得文件扩展名：('/path/to/file', '.txt')

print("对文件重命名")
os.rename('test.txt', 'test.py') #对文件重命名

print("删除文件")
os.remove('test.py') #删掉文件

print("列出当前目录下所有目录:")
print([x for x in os.listdir('.') if os.path.isdir(x)]) #列出当前目录下所有目录

print("列出当前目录下所有.py文件:")
print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py']) #列出当前目录下所有.py文件
'''
注意：
（1）把两个路径合成一个时，不要直接拼字符串，而要通过os.path.join()函数，
这样可以正确处理不同操作系统的路径分隔符，同样的道理，要拆分路径时，也不
要直接去拆字符串，而要通过os.path.split()函数，这样可以把一个路径拆分为
两部分，后一部分总是最后级别的目录或文件名；
（2）shutil模块提供了copyfile()的函数。
'''

print('      Size     Last Modified  Name')
print('------------------------------------------------------------')

for f in os.listdir(pwd):
    fsize = os.path.getsize(f)
    mtime = datetime.fromtimestamp(os.path.getmtime(f)).strftime('%Y-%m-%d %H:%M')
    flag = '/' if os.path.isdir(f) else ''
print('%10d  %s  %s%s' % (fsize, mtime, f, flag))
