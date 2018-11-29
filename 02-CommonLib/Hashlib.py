#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
此模块功能：hashlib提供了常见的摘要算法，如MD5，SHA1等等'''

__author__ = 'HouBin'

import hashlib

md5 = hashlib.md5()
md5.update('how to use md5 in python hashlib?'.encode('utf-8'))
print(md5.hexdigest())

sha1 = hashlib.sha1()
sha1.update('how to use sha1 in '.encode('utf-8'))
sha1.update('python hashlib?'.encode('utf-8'))
print(sha1.hexdigest())

import hmac
message = b'Hello, world!'
key = b'secret'
#注意传入的key和message都是bytes类型，str类型需要首先编码为bytes
h = hmac.new(key, message, digestmod='MD5')
# 如果消息很长，可以多次调用h.update(msg)
print(h.hexdigest())
