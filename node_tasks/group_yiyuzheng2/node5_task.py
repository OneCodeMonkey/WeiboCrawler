from tasks.user import crawl_person_infos
from tasks.home import crawl_weibo_datas
import time

# 混合
uids = [3130134533,2689620172,7281662606,1642237100,1774326455,5948625050,3959209351,2610310257,2433964232,7251109033,]

for uid in uids:
    crawl_person_infos(uid)

    crawl_weibo_datas(uid)
    time.sleep(11)


