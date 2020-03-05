import sys
import os
o_path = os.getcwd() # 返回当前工作目录
sys.path.append(o_path) # 添加自己指定的搜索路径

from tasks.user import crawl_person_infos
from tasks.home import crawl_weibo_datas
import time

# 全部（原创+转发）首页
uids = [5865752974,6582277668,5390283002,2449739667,2657767764,6260600122,5253880174,2830346285,5601943880,3100372123,2144686717,5179998040,5705237295,5719977898,6480083771,3836493233,3509207805,6816634930,6078283980,5528479466,
]

for uid in uids:
    crawl_person_infos(uid)

    crawl_weibo_datas(uid)
    time.sleep(1)