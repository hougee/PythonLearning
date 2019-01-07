#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
此模块功能：默认配置文件
'''


__author__ = 'HouBin'

configs = {
    'debug': True,
    'db': {
        'host': '127.0.0.1',
        'port': 3306,
        'user': 'root',
        'password': 'password',
        'db': 'awesome'
    },
    'session': {
        'secret': 'Awesome'
    }
}
