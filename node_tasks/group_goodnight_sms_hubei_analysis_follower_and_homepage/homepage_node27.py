import sys
import os
o_path = os.getcwd() # 返回当前工作目录
sys.path.append(o_path) # 添加自己指定的搜索路径

from tasks.user import crawl_person_infos
from tasks.home import crawl_weibo_datas
import time

# 全部（原创+转发）首页
uids = [5043379811,2659735117,2484801730,5453382095,2731282451,2423469043,5312734497,5976980416,1246548911,3959027919,6572440990,6155537378,6493944672,6598507740,5715379562,1882804934,1761505587,5541065045,7265749542,6571762355,1883228895,2486299184,3657675674,5583910544,2765489717,6475006582,6040951467,6601387510,1271850381,2358346840,2871613662,3159255940,5938182522,6612304132,6588814965,7138144455,6501678538,3938613314,5101471809,6596223021,6728103671,6856910056,5300254107,1070079444,3648582350,5889410618,2216729513,6008941026,6578577000,2245850264,5143726142,1445649957,7370159494,6407591504,5623134268,6798002205,5221200722,5769745541,5681296405,6583116808,1861332420,1784435620,2159312133,1114966267,

]

for uid in uids:
    crawl_person_infos(uid)

    crawl_weibo_datas(uid)
    time.sleep(1)