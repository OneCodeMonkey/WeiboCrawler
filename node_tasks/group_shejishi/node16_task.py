from tasks.user import crawl_person_infos
from tasks.home import crawl_weibo_datas
import time

# 设计师
uids = [2049997141,1849390867,1804546430,1784945467,1651964181,1702684702,1877332043,1247007923,1831898073,3939036953,3167201893,2414517074,1676156280,1628003391,5829631196,5338356108,]

for uid in uids:
    crawl_person_infos(uid)

    crawl_weibo_datas(uid)
    time.sleep(11)


