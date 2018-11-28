#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
功能说明：subprocess模块的使用：启动一个（外部）子进程，然后控制其输入和输出
'''

__author__ = 'HouBin'

import subprocess

print('$ nslookup')
p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE) #执行命令，也可直接用 r = subprocess.call(['nslookup', 'www.python.org'])
output, err = p.communicate(b'set q=mx\npython.org\nexit\n') #相当于执行命令后的手动输入
print(output.decode('utf-8'))
print('Exit code:', p.returncode)
