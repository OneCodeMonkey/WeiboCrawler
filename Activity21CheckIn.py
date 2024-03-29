# -*- coding=UTF-8 -*-
import requests
import time
import datetime
from logger import crawler

STARTTIME = '2019-10-21 00:00:00'
ENDTIME = '2019-10-21 20:00:00'
KEYWORD = '#21天挑战计划#'

start_time = datetime.datetime.strptime(STARTTIME, "%Y-%m-%d %H:%M:%S")
end_time = datetime.datetime.strptime(ENDTIME, "%Y-%m-%d %H:%M:%S")

OneHour = datetime.timedelta(hours=1)

time1 = start_time
time2 = start_time + OneHour


def get_topic_data(keyword, start_time='', end_time=''):
    from tasks.topic import search_keyword_topic
    search_keyword_topic(keyword, 33, start_time, end_time)


while 1:
    while time1 < end_time:
        start_time_str = time1.strftime("%Y-%m-%d-%H")
        end_time_str = time2.strftime("%Y-%m-%d-%H")
        print(start_time_str, '--', end_time_str)

        crawler.info("we are crawling keyword:{}, timerange {}:{} content" . format(KEYWORD, start_time_str, end_time_str))
        get_topic_data(KEYWORD, start_time_str, end_time_str)
        time1 = time1 + OneHour
        time2 = time2 + OneHour

    time1 = start_time
    time2 = start_time + OneHour

