#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
功能说明：Process类：代表一个进程对象
'''

__author__ = 'HouBin'

from multiprocessing import Process
import os,multiprocessing

# 子进程要执行的代码
def run_proc(name):
    print('Run child process %s (%s)...' % (name, os.getpid()))

if __name__=='__main__':
    print("The number of CPU in this computer:",multiprocessing.cpu_count())
    print('Parent process %s.' % os.getpid())
    p = Process(target=run_proc, args=('test',))
    print('Child process will start.')
    p.start()
    p.join()
    print('Child process end.')
