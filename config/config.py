#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
config.py

Author: ydn
Date: 20191111
Description:
    配置文件
"""


class Config(object):
    """
    扫描器配置类
    """
    CVE_API = {
        "username": "langke",
        "password": "langke,1234"
    }

    Wechat = {
        "app_id": "langke",
        "app_secret": "langke,1234"
    }

    MONGODB_CFG = {
        'host': '127.0.0.1',
        'port': 27017,
        'user': 'root',
        'passwd': 'langke',
        'data_db': 'bug_monitor',
        'table': 'SecurityProblem'
    }


CFG = Config()
