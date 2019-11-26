from tasks.user import crawl_person_infos
from tasks.home import crawl_weibo_datas
import time

# 设计师
uids = [6702903824,5770765700,5203199866,2361348251,2961303070,2796520357,3757388597,5842614109,6283760439,3236596874,1740214497,5966744714,2606639431,5958124866,1937381685,3789451110,]

for uid in uids:
    crawl_person_infos(uid)

    crawl_weibo_datas(uid)
    time.sleep(11)


