from tasks.user import crawl_person_infos
from tasks.home import crawl_weibo_datas
import time

# 混合
uids = [1766943190,2665729623,7342496300,3211590680,1946348547,5853217877,1812439705,2250520800,2678913063,5315259405,]

for uid in uids:
    crawl_person_infos(uid)

    crawl_weibo_datas(uid)
    time.sleep(11)


