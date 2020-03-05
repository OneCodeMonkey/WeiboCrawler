import sys
import os
o_path = os.getcwd() # 返回当前工作目录
sys.path.append(o_path) # 添加自己指定的搜索路径

from tasks.user import crawl_person_infos
from tasks.home import crawl_weibo_datas
import time

# 全部（原创+转发）首页
uids = [5841730031,6606650870,7389592749,6209716437,5239082918,7034935591,6616370633,6044704247,5880194712,6856782996,3967621566,6073479650,2068656671,6888661799,2274867894,2233745442,6783228996,1792357723,1638381323,7318919975,6129994159,

]

for uid in uids:
    crawl_person_infos(uid)

    crawl_weibo_datas(uid)
    time.sleep(1)