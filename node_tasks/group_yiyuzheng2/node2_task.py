from tasks.user import crawl_person_infos
from tasks.home import crawl_weibo_datas
import time

# 混合
uids = [1996623795,6390907884,2733759171,2640085723,2650773647,2097803371,5261314606,6645191527,6525436055,2698691821,]

for uid in uids:
    crawl_person_infos(uid)

    crawl_weibo_datas(uid)
    time.sleep(11)


