# -*- coding=UTF-8 -*-
import requests

def get_topic_data():
    from tasks.topic import search_keyword_topic
    search_keyword_topic("#一般人驾驭不了的芭比粉#", 33)

get_topic_data()