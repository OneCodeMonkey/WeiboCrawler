# -*- coding=UTF-8 -*-
import requests
import time
import datetime

STARTTIME = '2019-09-01 00:00:00'
ENDTIME = '2019-09-09 12:00:00'

start_time = datetime.datetime.strptime(STARTTIME, "%Y-%m-%d %H:%M:%S");
end_time = datetime.datetime.strptime(ENDTIME, "%Y-%m-%d %H:%M:%S");

OneHour = datetime.timedelta(hours=1)

time1 = start_time
time2 = start_time + OneHour

while time1 < end_time:
    print(time1.strftime("%Y-%m-%d-%H"), '--', time2.strftime("%Y-%m-%d-%H"))
    time1 = time1 + OneHour
    time2 = time2 + OneHour



def get_topic_data():
    from tasks.topic import search_keyword_topic
    search_keyword_topic("#一般人驾驭不了的芭比粉#", 33, '', '')

get_topic_data()