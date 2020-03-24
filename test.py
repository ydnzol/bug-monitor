#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : mr.chery (mr.chery666@gmail.com)
import datetime
from pymongo import MongoClient
from dateutil.relativedelta import relativedelta
from config.config import CFG

host = CFG.MONGODB_CFG['host']
username = CFG.MONGODB_CFG['user']
password = CFG.MONGODB_CFG['passwd']
port = int(CFG.MONGODB_CFG['port'])
db = CFG.MONGODB_CFG['data_db']
mongo_url = 'mongodb://{0}:{1}@{2}:{3}/?authSource={4}&authMechanism=SCRAM-SHA-1'.format(
    username, password, host, port, db)
clinet = MongoClient(mongo_url)


def conn_mongo():
    conn = MongoClient(CFG.MONGODB_CFG['host'], int(CFG.MONGODB_CFG['port']))
    db = conn[CFG.MONGODB_CFG['data_db']]
    db.authenticate(CFG.MONGODB_CFG['user'],
                    CFG.MONGODB_CFG['passwd'])
    return db


def bug_info_search():
    # db = clinet[CFG.MONGODB_CFG['data_db']]
    db = conn_mongo()
    print(type(db))
    database = db[CFG.MONGODB_CFG['table']]
    x = database.find_one()
    print(x, type(x))


if __name__ == '__main__':
    bug_info_search()
