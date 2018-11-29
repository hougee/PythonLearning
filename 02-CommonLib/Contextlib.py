#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
此模块功能：contextlib模块实现上下文管理（可以使用with）'''

__author__ = 'HouBin'

#通过__enter__和__exit__两个方法实现上下文管理
class Query1(object):

    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print('Begin1')
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type:
            print('Error1')
        else:
            print('End1')

    def query(self):
        print('Query1 info about %s...' % self.name)

with Query1('Bob') as q:
    q.query()

#通过@contextmanager实现上下文管理
from contextlib import contextmanager

class Query2(object):

    def __init__(self, name):
        self.name = name

    def query(self):
        print('Query2 info about %s...' % self.name)

@contextmanager
def create_query(name):
    print('Begin2')
    q = Query2(name)
    yield q
    print('End2')

with create_query('Bob') as q:
    q.query()

#通过@contextmanager实现在某段代码执行前后自动执行特定代码
@contextmanager
def tag(name):
    print("<%s>" % name)
    yield
    print("</%s>" % name)

with tag("h1"):
    print("hello")
    print("world")

#通过closing()将没有实现上下文的对象转换为上下文对象
from contextlib import closing
from urllib.request import urlopen

with closing(urlopen('https://www.python.org')) as page:
    for line in page:
        print(line)
