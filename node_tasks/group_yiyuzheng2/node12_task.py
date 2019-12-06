from tasks.user import crawl_person_infos
from tasks.home import crawl_weibo_datas
import time

# 混合
uids = [5943167550,7193352793,6013903946,3316014095,2681077970,5613830059,5629649827,5514616170,7166642476,5747538013,]

for uid in uids:
    crawl_person_infos(uid)

    crawl_weibo_datas(uid)
    time.sleep(11)


