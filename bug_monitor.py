#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : mr.chery (mr.chery666@gmail.com)
import requests
from struts import struts_check
from struts import struts_init
from seebug import seebug_crawler
from cve import cve_crawler
from threading import Timer
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


def struts_monitor():
    time = 60 * 5
    struts_check()
    t = Timer(time, struts_monitor)
    t.start()


def seebug_monitor():
    time = 60 * 60 * 6
    seebug_crawler()
    t = Timer(time, seebug_monitor)
    t.start()


def cve_monitor():
    time = 60 * 60 * 6
    cve_crawler()
    t = Timer(time, cve_monitor)
    t.start()


if __name__ == '__main__':
    struts_init()
    struts_monitor()
    seebug_monitor()
    cve_monitor()
