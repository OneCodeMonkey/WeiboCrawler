from tasks.user import crawl_person_infos
from tasks.home import crawl_weibo_datas
import time

# 设计师
uids = [2994673875,6854011249,5797834881,5528654701,2027895057,3911354673,5083516199,3540651234,6867263255,2135686773,5522484119,5055199012,1906904747,5382618347,5943114932,2487177671,]

for uid in uids:
    crawl_person_infos(uid)

    crawl_weibo_datas(uid)
    time.sleep(11)


