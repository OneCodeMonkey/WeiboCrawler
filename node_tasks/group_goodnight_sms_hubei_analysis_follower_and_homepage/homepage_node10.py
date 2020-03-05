import sys
import os
o_path = os.getcwd() # 返回当前工作目录
sys.path.append(o_path) # 添加自己指定的搜索路径

from tasks.user import crawl_person_infos
from tasks.home import crawl_weibo_datas
import time

# 全部（原创+转发）首页
uids = [5298005381,1960362647,7322184576,6856766832,2375338275,6085450202,2945855332,2194512761,1883228895,1070079444,6583116808,5644946000,7320946519,2021602811,6091172528,5333975624,6355775928,6439562925,6011522808,
]

for uid in uids:
    crawl_person_infos(uid)

    crawl_weibo_datas(uid)
    time.sleep(1)