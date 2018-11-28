#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
功能说明：Pool类：用进程池的方式批量创建子进程（需要使用命令行运行）
'''

__author__ = 'HouBin'

from multiprocessing import Pool
import os, time, random

def long_time_task(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))

if __name__=='__main__':
    print('Parent process %s.' % os.getpid())
    p = Pool(4) #设置进程池同时执行进程的数量
    for i in range(5):
        p.apply_async(long_time_task, args=(i,))
    print('Waiting for all subprocesses done...')
    p.close() #调用join()之前必须先调用close()，调用close()之后就不能继续添加新的Process
    p.join() #对Pool对象调用join()方法会等待所有子进程执行完毕
    print('All subprocesses done.')
