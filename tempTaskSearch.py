# -*- coding=UTF-8 -*-
import requests
import time
import datetime
from logger import crawler

topics = ["#双11快递员每人每天送240件快递#", "#人民空军成立70周年#", "#双十一#", "#购物津贴没用上#", "#买买买之后最该看的微博#", "#买买买之后最该看的微博#", "#光棍节#", "#心愿大奖#", "#男生把宿舍装成酒店风#", "#送人民空军上热搜#", "#韩国重启世越号调查#", "#高中生用函数模型做双11攻略#", "#要吃土了#", "#香港特区政府就暴徒破坏行为发声#", "#江姐托孤信曝光#"]

for topic in topics:
    STARTTIME = '2019-11-08 06:00:00'
    ENDTIME = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    KEYWORD = topic

    start_time = datetime.datetime.strptime(STARTTIME, "%Y-%m-%d %H:%M:%S")
    end_time = datetime.datetime.strptime(ENDTIME, "%Y-%m-%d %H:%M:%S")

    OneHour = datetime.timedelta(hours=1)

    time1 = start_time
    time2 = start_time + OneHour


    def get_topic_data(keyword, start_time='', end_time=''):
        from tasks.topic import search_keyword_topic
        search_keyword_topic(keyword, 33, start_time, end_time)


    while time1 < end_time:
        start_time_str = time1.strftime("%Y-%m-%d-%H")
        end_time_str = time2.strftime("%Y-%m-%d-%H")
        print(start_time_str, '--', end_time_str)

        crawler.info("we are crawling keyword:{}, timerange {}:{} content" . format(KEYWORD, start_time_str, end_time_str))
        get_topic_data(KEYWORD, start_time_str, end_time_str)
        time1 = time1 + OneHour
        time2 = time2 + OneHour
