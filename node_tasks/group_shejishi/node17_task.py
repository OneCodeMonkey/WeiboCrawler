from tasks.user import crawl_person_infos
from tasks.home import crawl_weibo_datas
import time

# 设计师
uids = [2377172040,1680551132,6394121666,2118389107,1790162752,2652927102,1806306700,2236357313,1607583842,5263382915,1974685845,2704468945,1276815035,1623165465,2834463372,2518254411,]

for uid in uids:
    crawl_person_infos(uid)

    crawl_weibo_datas(uid)
    time.sleep(11)


