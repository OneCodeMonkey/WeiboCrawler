from urllib import parse as url_parse

from .logger import crawler
from .workers import app
from page_get import get_page
from config import get_max_search_page
from db.dao import (KeywordsOper, KeywordsDataOper, WbDataOper)

def execute_topic_task():
