#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
数据库相关操作
Author: lqy
Date: 20180604
"""
import json
import logging
#import MySQLdb
import time
from logger import get_logger
from pymongo import MongoClient
from logger import get_logger
from config.config import CFG

logger = get_logger('', CFG.AUTO_UPGRADE_DIRS['LOG_DIR'], CFG.AUTO_UPGRADE_DIRS['LOG_FILE'], logging.INFO)

class DBClient(object):
    def __init__(self, logger):
        self.db_instance = PyMongo(logger)
    def __del__(self):
        """
        关闭数据库
        :return:
        """
        self.db_instance.close_connection()

    def add_data(self, data):
        ret = self.db_instance.insert_data(data)
        return ret

    def set_data(self, data):
        ret = self.db_instance.set_data(data)
        return ret

    def del_data(self, data):
        ret = self.db_instance.set_data(data)
        return ret


class PyMongo(object):
    def __init__(self, logger):
        self.client = None
        self.db = None
        self.logger = logger
        self.connect_mongo()

    def connect_mongo(self):
        try:
            self.client = MongoClient(CFG.MONGODB_CFG['host'], int(CFG.MONGODB_CFG['port']))
            self.db = self.client[CFG.MONGODB_CFG['data_db']]
            self.db.authenticate(CFG.MONGODB_CFG['user'],
                                 CFG.MONGODB_CFG['passwd'])  # 认证用户名
        except Exception as err:
            self.logger.error('connect_mongo failed! reason:%s', err)
            return False
        return True

    def close_connection(self):
        if self.client:
            self.client.close()

    def insert_data(self, data):
        try:
            data_json = json.loads(data)
            insert_data = data_json['data']
            insert_data['MSPInsertDate'] = time.strftime('%Y-%m-%d %H:%M:%S')
            _id = self.db[CFG.MONGODB_CFG['table']].insert(insert_data)
        except Exception as err:
            self.logger.error('insert_data failed! reason:%s', err)
            return False
        return True

    def add_data(self, table, data):
        try:
            self.logger.info('Table:%s add_data:%s', table, data)
            self.db[table].insert(data)
        except Exception as err:
            self.logger.error('add_data failed! table:{} data:{} err:{}'
                              .format(table, data, err))
            return False
        return True

    def find_data(self, data):
        ret = self.db_instance.find_data(data)
        return ret

    def set_data(self, data):
        try:
            data_json = json.loads(data)
            cond = data_json['cond']
            insert_data = data_json['data']
            _id = self.db[CFG.MONGODB_CFG['table']].update(cond, {'$set': insert_data}, True, True)
        except Exception as err:
            self.logger.error('set_data failed! reason:%s', err)
            return False
        return True



