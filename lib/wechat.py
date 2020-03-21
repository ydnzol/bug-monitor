#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : mr.chery (mr.chery666@gmail.com)
from werobot import WeRoBot
from config.config import CFG

robot = WeRoBot()

robot.config["APP_ID"] = CFG.Wechat["app_id"]
robot.config["APP_SECRET"] = CFG.Wechat["app_secret"]

client = robot.client


def send_wechat(info):
    followers_info = client.get_followers()
    followers_list = followers_info['data']['openid']
    for follower in followers_list:
        client.send_text_message(follower, info)
