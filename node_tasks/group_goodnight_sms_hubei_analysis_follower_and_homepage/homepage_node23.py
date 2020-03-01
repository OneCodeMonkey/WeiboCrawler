import sys
import os
o_path = os.getcwd() # 返回当前工作目录
sys.path.append(o_path) # 添加自己指定的搜索路径

from tasks.user import crawl_person_infos
from tasks.home import crawl_weibo_datas
import time

# 全部（原创+转发）首页
uids = [2778898300,6584777332,3265798025,6658195953,1960362647,2776074893,5935237518,2951680937,3721354360,1838540517,5217386710,6246839463,6396471027,6088365117,7040971953,6042895385,6620437639,2814050844,7304016677,7285361037,6072065319,2993753797,6232112101,6913456349,7329504666,3001843353,6597454663,5850772063,5672965217,5890194094,6449175095,5678338928,2064266177,1763055372,2085282913,7322184576,6856766832,6505429944,5910004003,5664488897,5648499258,6675328996,5756123934,6618877424,5615786218,5312241795,5259397329,6615251824,1412841560,6131059582,5682192500,6887365146,1596684260,7303323896,6667672589,5633563765,5632664231,6001086818,3929623514,2499844853,1956636004,6613226939,7039860614,2177821742,

]

for uid in uids:
    crawl_person_infos(uid)

    crawl_weibo_datas(uid)
    time.sleep(1)