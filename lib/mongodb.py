#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : mr.chery (mr.chery666@gmail.com)
import datetime
from pymongo import MongoClient
from dateutil.relativedelta import relativedelta
from config.config import CFG


def conn_mongo():
    conn = MongoClient(CFG.MONGODB_CFG['host'], int(CFG.MONGODB_CFG['port']))
    db = conn[CFG.MONGODB_CFG['data_db']]
    db.authenticate(CFG.MONGODB_CFG['user'],
                    CFG.MONGODB_CFG['passwd'])
    return db


def bug_info_save(name, rate, affected, info, cveid, url, addtime):
    db = conn_mongo()
    table = CFG.MONGODB_CFG['table']
    collections = db[table]
    data = {
        'name': name,
        'rate': rate,
        'affected': affected,
        'info': info,
        'cveid': cveid,
        'url': url,
        'addtime': addtime,
    }
    collections.insert(data)
    bug_early_clean()


def bug_info_search(name):
    db = conn_mongo()
    database = db[CFG.MONGODB_CFG['table']]
    return database.find_one({"name": name})


def cve_info_save(name, cveid, url, addtime):
    db = conn_mongo()
    database = db[CFG.MONGODB_CFG['table']]
    data = {
        'name': name,
        'cveid': cveid,
        'url': url,
        'addtime': addtime,
    }
    database.insert(data)
    bug_early_clean()


def cve_info_search(cveid):
    db = conn_mongo()
    database = db[CFG.MONGODB_CFG['table']]
    return database.find_one({"cveid": cveid})


def bug_early_clean():
    db = conn_mongo()
    database = db[CFG.MONGODB_CFG['table']]
    before_data = datetime.date.today() - relativedelta(months=+1)
    early = before_data.strftime("%Y-%m-%d")
    database.remove({"addtime": {"$lt": early}})
