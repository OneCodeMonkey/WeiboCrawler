# -*- coding=UTF-8 -*-
import requests

def get_search_data():
    from tasks.search import search_keyword
    search_keyword("#香港事件#",5)

get_search_data()