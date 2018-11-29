#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
此模块功能：Base64是一种用64个字符来表示任意二进制数据的方法，常用于在URL、Cookie、网页中传输少量二进制数据。
'''

__author__ = 'HouBin'

import base64

s = base64.b64encode('在Python中使用BASE 64编码'.encode('utf-8'))
print(s)
d = base64.b64decode(s).decode('utf-8')
print(d)

s = base64.urlsafe_b64encode('在Python中使用BASE 64编码'.encode('utf-8'))
print(s)
d = base64.urlsafe_b64decode(s).decode('utf-8')
print(d)
