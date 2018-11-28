#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
功能说明：fork()的使用（不可用于windows系统）
'''

__author__ = 'HouBin'

import os

print('Process (%s) start...' % os.getpid())
# Only works on Unix/Linux/Mac:
pid = os.fork()
'''
Unix/Linux操作系统提供了一个fork()系统调用，fork()调用一次，
返回两次，因为操作系统自动把当前进程（称为父进程）复制了一
份（称为子进程），然后，分别在父进程和子进程内返回。子进程
永远返回0，而父进程返回子进程的ID。
'''
if pid == 0:
    print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
else:
    print('I (%s) just created a child process (%s).' % (os.getpid(), pid))
