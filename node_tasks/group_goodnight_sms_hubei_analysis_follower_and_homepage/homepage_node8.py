import sys
import os
o_path = os.getcwd() # 返回当前工作目录
sys.path.append(o_path) # 添加自己指定的搜索路径

from tasks.user import crawl_person_infos
from tasks.home import crawl_weibo_datas
import time

# 全部（原创+转发）首页
uids = [5735394841,6427351227,5668885350,1653618321,5473751128,5521663700,6768766122,6167698721,7302245522,6375594636,1944927414,6602215463,6076253054,1847067290,5508520910,1882886573,3060183607,6205891817,6781608566,3278643397,
]

for uid in uids:
    crawl_person_infos(uid)

    crawl_weibo_datas(uid)
    time.sleep(1)