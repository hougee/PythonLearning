#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'此模块功能：内建模块collections中的ChainMap'

__author__ = 'HouBin'

from collections import ChainMap
import os, argparse

# 构造缺省参数
defaults = {
    'color': 'red',
    'user': 'guest'
}

# 构造命令行参数
parser = argparse.ArgumentParser()
parser.add_argument('-u', '--user')
parser.add_argument('-c', '--color')
namespace = parser.parse_args()
command_line_args = { k: v for k, v in vars(namespace).items() if v }

# 组合成ChainMap：ChainMap可以把一组dict串起来并组成一个逻辑上
#的dict。ChainMap本身也是一个dict，但是查找的时候，会按照顺序在
#内部的dict依次查找
combined = ChainMap(command_line_args, os.environ, defaults)

# 打印参数:
print('color=%s' % combined['color'])
print('user=%s' % combined['user'])


#具体使用方法如下：
#没有任何参数时，打印出默认参数，命令行输入：python3 use_chainmap.py
#当传入命令行参数时，优先使用命令行参数，命令行输入：python3 use_chainmap.py -u bob
#同时传入命令行参数和环境变量，命令行参数的优先级较高，命令行输入：user=admin color=green python3 use_chainmap.py -u bob
