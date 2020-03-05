import sys
import os
o_path = os.getcwd() # 返回当前工作目录
sys.path.append(o_path) # 添加自己指定的搜索路径

from tasks.user import crawl_person_infos
from tasks.home import crawl_weibo_datas
import time

# 全部（原创+转发）首页
uids = [3807019240,6620217822,5780517784,1492340484,5784959517,7163812728,3567121004,3187313962,6728414746,5880810853,3833210370,6719939876,3246203300,6672510141,2118737520,6994261871,5838245297,1939307901,2953343793,2745653947,3040616203,
]

for uid in uids:
    crawl_person_infos(uid)

    crawl_weibo_datas(uid)
    time.sleep(1)