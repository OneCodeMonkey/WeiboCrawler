from tasks.user import crawl_person_infos
from tasks.home import crawl_weibo_datas
import time

# 混合
uids = [3302098561,1833431450,5846608768,2728830773,6347489303,3206470453,5174233355,6137004325,2734782651,5102707683,]

for uid in uids:
    crawl_person_infos(uid)

    crawl_weibo_datas(uid)
    time.sleep(11)


