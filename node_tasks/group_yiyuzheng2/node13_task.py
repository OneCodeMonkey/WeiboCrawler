from tasks.user import crawl_person_infos
from tasks.home import crawl_weibo_datas
import time

# 混合
uids = [2956343732,5293417781,5133494480,2541832445,1780065374,2159136581,2515321443,5534505916,5352438454,1012241847,]

for uid in uids:
    crawl_person_infos(uid)

    crawl_weibo_datas(uid)
    time.sleep(11)


