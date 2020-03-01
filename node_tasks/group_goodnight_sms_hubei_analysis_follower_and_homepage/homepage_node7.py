import sys
import os
o_path = os.getcwd() # 返回当前工作目录
sys.path.append(o_path) # 添加自己指定的搜索路径

from tasks.user import crawl_person_infos
from tasks.home import crawl_weibo_datas
import time

# 全部（原创+转发）首页
uids = [5556601688,6273314282,2675098820,6192062656,5285890205,6797777734,6155408921,6610277614,6476826602,3959333095,5029146151,6866119135,6562080232,6875163957,7317954095,6054430786,2038270375,5735240342,7247501278,7310543941,5884311213,2353579021,7311385947,5744931745,3411059854,6196263793,1417151523,6486066811,5280166811,5947281688,6606385480,6425364074,7247118713,3674388837,6323592295,1695414227,6200070173,6777211685,6892952965,1846839354,5223870378,6444070638,6039238800,7293578653,6070389988,3195470953,6678763319,3666524187,6451913039,6268133225,7313063978,6174872932,6005709305,6003664899,6833631418,6821068318,6836909017,7318604114,6596094937,5993887877,1243931214,5997851039,5750277411,6797874248,

]

for uid in uids:
    crawl_person_infos(uid)

    crawl_weibo_datas(uid)
    time.sleep(1)