#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : mr.chery (mr.chery666@gmail.com)

import requests
import time
from config.config import CFG
from lib.mongodb import *
from lib.log import *

url = "https://api.saucs.com/cve"


def cve_crawler():
    req = requests.Session()
    try:
        cve_list = req.get(url, auth=(CFG["CVE_API"]["username"],
                                      CFG["CVE_API"]["password"]),
                           timeout=5)
    except Exception as e:
        exception(e)
    a = cve_list.json()
    for i in range(len(a)):
        try:
            cve_url = url + '/' + a[i]['name']
            cve_info_page = req.get(cve_url, auth=(CFG["CVE_API"]["username"],
                                                   CFG["CVE_API"]["password"]),
                                    timeout=5)
            cve_info = cve_info_page.json()
            refer = cve_info['references'][0]['link']
            cveid = cve_info['name']
            summary = cve_info['summary']
            if not cve_info_search(cveid):
                addtime = time.strftime(
                    '%Y-%m-%d', time.localtime(time.time()))
                cve_info_save(summary, cveid, refer, addtime)
            info("cve info save success")
        except Exception as e:
            exception(e)
            info("your cve api auth may be wrong")
