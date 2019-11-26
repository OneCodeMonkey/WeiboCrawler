from tasks.user import crawl_person_infos
from tasks.home import crawl_weibo_datas
import time

# 设计师
uids = [2671752953,5985871120,2650459275,5559994421,6501726394,5780295881,5736520959,2519590514,5665300401,1319473347,5646279889,1907042331,3879623308,6408216915,3240884914,5362419513,]

for uid in uids:
    crawl_person_infos(uid)

    crawl_weibo_datas(uid)
    time.sleep(11)


