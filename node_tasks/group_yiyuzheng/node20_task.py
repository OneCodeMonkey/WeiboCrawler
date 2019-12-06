from tasks.user import crawl_person_infos
from tasks.home import crawl_weibo_datas
import time

# 混合
uids = [6319489043,3192849372,5683360842,6379052191,5375438590,6988462876,5288291243,6491327366,5716035048,1941171713,6579420376,6508239940,5259676743,6903978891,6414263743,6765892153,]

for uid in uids:
    crawl_person_infos(uid)

    crawl_weibo_datas(uid)
    time.sleep(11)


