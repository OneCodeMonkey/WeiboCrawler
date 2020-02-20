import sys
import os
o_path = os.getcwd() # 返回当前工作目录
sys.path.append(o_path) # 添加自己指定的搜索路径

from logger import crawler
from tasks.workers import app
from tasks.search import search_keyword

KEYWORDS = [
    "想死 肺炎",
]

for KEYWORD in KEYWORDS:
    crawler.info("sending searching task with keyword:" + str(KEYWORD))
    search_keyword(KEYWORD, 1)