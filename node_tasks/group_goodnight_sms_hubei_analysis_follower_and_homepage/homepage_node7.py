import sys
import os
o_path = os.getcwd() # 返回当前工作目录
sys.path.append(o_path) # 添加自己指定的搜索路径

from tasks.user import crawl_person_infos
from tasks.home import crawl_weibo_datas
import time

# 全部（原创+转发）首页
uids = [1403406967,5534509938,5780370346,6180848840,5736171397,5255280461,6579329465,1730411387,2797120900,3204890992,6784934258,5278185015,5595181778,5852140462,2184593501,6035127444,2385265611,7310125691,5516605981,2311758364,
]

for uid in uids:
    crawl_person_infos(uid)

    crawl_weibo_datas(uid)
    time.sleep(1)