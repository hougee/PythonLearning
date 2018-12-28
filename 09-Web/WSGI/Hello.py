#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'此模块功能：最简单的BS程序'

__author__ = 'HouBin'

def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    body = '<h1>Hello, %s!</h1>' % (environ['PATH_INFO'][1:] or 'web')
    return [body.encode('utf-8')]
