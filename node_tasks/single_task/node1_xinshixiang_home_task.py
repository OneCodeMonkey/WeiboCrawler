from tasks.user import crawl_person_infos
from tasks.home import crawl_weibo_datas
import time

uids = [3818859252]

for uid in uids:
    crawl_person_infos(uid)

    crawl_weibo_datas(uid)
    time.sleep(11)