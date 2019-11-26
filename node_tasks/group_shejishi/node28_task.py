from tasks.user import crawl_person_infos
from tasks.home import crawl_weibo_datas
import time

# 设计师
uids = [6349370525,3214115193,5232150073,1772019010,6873494617,6343826569,5236541311,5920941684,5858737829,6359577955,5570235872,5646828597,1768796262,5170987627,1947462144,5479499013,]

for uid in uids:
    crawl_person_infos(uid)

    crawl_weibo_datas(uid)
    time.sleep(11)


