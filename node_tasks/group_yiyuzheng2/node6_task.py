from tasks.user import crawl_person_infos
from tasks.home import crawl_weibo_datas
import time

# 混合
uids = [3248713474,6343807260,6215491447,6046084112,3953528488,5656022392,5841323346,3282922202,7084510888,6028553894,]

for uid in uids:
    crawl_person_infos(uid)

    crawl_weibo_datas(uid)
    time.sleep(11)


