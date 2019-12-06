from tasks.user import crawl_person_infos
from tasks.home import crawl_weibo_datas
import time

# 混合
uids = [2279256182,5215220058,1724222727,2746162371,2493710472,1975038237,3153207465,2774735987,2169895381,2604273495,]

for uid in uids:
    crawl_person_infos(uid)

    crawl_weibo_datas(uid)
    time.sleep(11)


