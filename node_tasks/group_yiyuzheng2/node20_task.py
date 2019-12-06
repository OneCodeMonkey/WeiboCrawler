from tasks.user import crawl_person_infos
from tasks.home import crawl_weibo_datas
import time

# 混合
uids = [5623685382,5234025450,5586662034,5498334562,2463794591,2964494493,]

for uid in uids:
    crawl_person_infos(uid)

    crawl_weibo_datas(uid)
    time.sleep(11)


