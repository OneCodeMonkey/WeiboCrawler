# -*- coding=UTF-8 -*-
import requests
import time
import datetime
from logger import crawler

topics = ["#大连行凶男孩舅舅首发声#", "#大连被害女孩曾写信给父母#", "#67岁孕妇自然受孕产女#", "#大连男孩被曝多次尾随女性#", "#15岁中学生砖头打老师被刑拘#", "#日本天价柿子两个5万元#", "#为何未成年人低龄化犯罪频发#", "#14个越南家庭报案家人疑失踪英国#", "#当撒贝宁遇上康辉#", "#大连遇害女童家属聘请律师#", "#英货车藏尸案已逮捕4人#", "#地铁内使用电子产品不许外放#", "#今天环卫工人节#", "#国家要求减少地铁火车站重复安检#"]

for topic in topics:
    STARTTIME = '2019-10-26 11:00:00'
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
