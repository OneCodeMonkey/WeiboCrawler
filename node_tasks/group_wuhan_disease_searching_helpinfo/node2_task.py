import sys
import os
o_path = os.getcwd() # 返回当前工作目录
sys.path.append(o_path) # 添加自己指定的搜索路径

from logger import crawler
from tasks.workers import app
from tasks.search import search_keyword

KEYWORDS = [
    "武汉 疫情",
    "爸爸 医院",
    "妈妈 医院",
    "武汉 肺炎",
    "肺炎 求助",
    "武汉 求助",
    "黄冈 求助",
    "黄冈 肺炎",
    "孝感 肺炎",
    "孝感 求助",
    "湖北 肺炎",
    "湖北 求助",
    "肺炎患者求助",
    "肺炎 住院",
    "求助 住院",
    "武汉 住院",
]

while 1:
    for KEYWORD in KEYWORDS:
        crawler.info("sending searching task with keyword:" + str(KEYWORD))
        search_keyword(KEYWORD, 1)