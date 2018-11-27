#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
功能说明：通过命令行为运行程序添加参数
需要模块：sys
参数个数：len(sys.argv)
文件名：    sys.argv[0]
参数1：     sys.argv[1]
参数2：     sys.argv[2]
......
'''

__author__ = 'HouBin'

import sys
print("file = ", sys.argv[0])
for i in range(1, len(sys.argv)):
    print("parameter%s = %s"%(i, sys.argv[i]))