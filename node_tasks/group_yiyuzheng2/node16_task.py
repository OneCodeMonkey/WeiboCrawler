from tasks.user import crawl_person_infos
from tasks.home import crawl_weibo_datas
import time

# 混合
uids = [3925988616,3848269748,2979386582,3741316952,1809487427,1751727394,3828295068,3205992387,6011150834,6374395022,]

for uid in uids:
    crawl_person_infos(uid)

    crawl_weibo_datas(uid)
    time.sleep(11)


