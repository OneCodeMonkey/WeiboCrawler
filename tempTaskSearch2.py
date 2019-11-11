# -*- coding=UTF-8 -*-
import requests
import time
import datetime
from logger import crawler

topics = ["#生活中有哪些简单的快乐#", "#双十一前后的真实写照#", "#双十一后的常见表现#", "#女人的钱花在哪了#", "#如何兼顾好事业与爱情#", "#一句话形容双十一之后的你#", "#一次奇怪的吵架经历#", "#双十一真的省钱吗#", "#你希望你的前任好吗#", "#你的双十一清单#", "#双十一不要忘记你是单身#", "#小巫塔罗#", "#大学毕业该怎么择业#"]

for topic in topics:
    STARTTIME = '2019-10-20 11:00:00'
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
