import sys
import os
o_path = os.getcwd() # 返回当前工作目录
sys.path.append(o_path) # 添加自己指定的搜索路径

from tasks.user import crawl_person_infos
from tasks.home import crawl_weibo_datas
import time

# 全部（原创+转发）首页
uids = [6426225577,6318339150,5638642227,2815990094,6499655600,6677614661,2793323943,1155777307,3653448467,2755892935,3707464664,6607353712,5974370437,6866530091,2071755383,1663140620,6537594513,1656604924,3660932287,3355396712,1715984205,
]

for uid in uids:
    crawl_person_infos(uid)

    crawl_weibo_datas(uid)
    time.sleep(1)