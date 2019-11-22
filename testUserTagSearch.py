import requests
import time
import datetime
from logger import crawler
from tasks.userTagSearch import search_user_tag_list

tags = [
    "创造力",
    "游戏",
    "想象力",
    "好奇心",
    "潮流时尚",
    "个性",
    "艺术",
    "创新",
    "跨界",
    "新奇",
    "科幻",
    "外星人",
    "gamer",
    "电竞",
    "虚拟",
    "宇宙",
    "NARS",
    "独特",
    "不一样",
    "酷",
    "电竞",
    "剪辑后期",
    "音乐创作者",
    "程序员",
    "文字工作者",
]

for tag in tags:
    search_user_tag_list(tag)