import re
import urllib.parse
import time
from datetime import datetime
import datetime

from bs4 import BeautifulSoup

from logger import parser
from page_parse import status
from utils import url_filter
from db.models import User
from decorators import parse_decorator
from tasks.workers import app
from config import(get_crawling_mode, get_images_allow, get_images_path)

CRAWLING_MODE = get_crawling_mode()
IMG_ALLOW = get_images_allow()
IMG_PATH = get_images_path()

@parse_decorator('')
def get_user_tag_search_info(html):
    content = html
    soup = BeautifulSoup(content.encode('utf-8', 'ignore').decode('utf-8'), "html.parser")
    user_list = soup.find_all(attrs={'class':'s-btn-c'})
    # for item in user_list:
    #     print(item)

    return user_list