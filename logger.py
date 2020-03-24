#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
logger.py

Author: zeusguy
Date: 20171108
"""
import logging
import os
import re
import time

from logging import StreamHandler
from logging.handlers import RotatingFileHandler
from logging.handlers import TimedRotatingFileHandler


def get_logger(logger_name, log_dir, fname,
               level=logging.INFO,
               type=1):
    """获取日志logger。

    Args:
        logger_name: logger名称
        log_dir: 日志基础路径
        fname: 日志文件名称字符串
        level: 日志级别
        type: 取值1-TimeRotatingFileHandler、2-RotatingFileHandler、3-StreamHandler
    """
    log_dir = os.path.join(log_dir, logger_name)
    if not os.path.isdir(log_dir):
        os.makedirs(log_dir)

    log_fmt = '[%(asctime)s][%(levelname)s][%(filename)s]%(message)s'
    date_fmt = '%Y-%m-%d %H:%M:%S'
    formatter = logging.Formatter(log_fmt, date_fmt)

    logger = logging.getLogger(logger_name)
    logger.setLevel(level)

    if type == 1:
        date_now = time.strftime("%Y-%m-%d", time.localtime(time.time()))
        log_file = os.path.join(log_dir, ''.join([fname, '_', date_now + '.log']))
        if not os.path.exists(log_file):
            tmp_file = open(log_file, "w")
            tmp_file.close()
        log_handler = TimedRotatingFileHandler(filename=log_file, 
                                               when='midnight',
                                               interval=1,
                                               backupCount=7)
        log_handler.suffix = "%Y-%m-%d.log"
        log_handler.extMatch = re.compile(r"^\d{4}-\d{2}-\d{2}\.log")
    elif type == 2:
        log_file = os.path.join(log_dir, fname)
        if not os.path.exists(log_file):
            tmp_file = open(log_file, "w")
            tmp_file.close()
        log_handler = RotatingFileHandler(filename=log_file, mode='a', 
                                          maxBytes=1024*1024*2, backupCount=1)
    else:
        log_handler = StreamHandler()

        
    log_handler.setFormatter(formatter)
    logger.setLevel(level)
    logger.addHandler(log_handler)

    return logger


if __name__ == '__main__':
    logger = get_logger('test', '/usability/log', 'hello', type=2)
    logger.info("JUST FOR TEST!")
    logger.info("HELLO WORLD")
