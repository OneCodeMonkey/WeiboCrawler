import sys
import os
o_path = os.getcwd() # 返回当前工作目录
sys.path.append(o_path) # 添加自己指定的搜索路径

from tasks.user import crawl_person_infos
from tasks.home import crawl_weibo_datas
import time

# 全部（原创+转发）首页
uids = [6775093054,6631388516,6276339413,6193688857,6070314801,5232275463,6285695570,5838061985,7225275783,6607289115,5092122595,5264691827,5948817787,7066358647,6596908310,1941076097,2567095773,5840227609,2683584587,5857545837,5285313324,
]

for uid in uids:
    crawl_person_infos(uid)

    crawl_weibo_datas(uid)
    time.sleep(1)