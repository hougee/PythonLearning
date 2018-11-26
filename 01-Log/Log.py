#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'此模块功能：生成日志'

__author__ = 'HouBin'

import logging

#日志格式化输出
LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
# 创建一个handler，用于写入日志文件
fh = logging.FileHandler('test.log')
# 再创建一个handler，用于输出到控制台
ch = logging.StreamHandler()
#配置日志基本参数
logging.basicConfig(level=logging.DEBUG, format=LOG_FORMAT, handlers=[fh, ch])
# 创建一个logger
logger = logging.getLogger('mylogger')
# 记录一条日志
logger.info('基本日志信息')
logger.debug('调试日志信息')
logger.warning('警告日志信息')
logger.error('错误日志信息')
logger.critical('批评日志信息')
