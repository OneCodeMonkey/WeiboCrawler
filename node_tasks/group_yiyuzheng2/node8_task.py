from tasks.user import crawl_person_infos
from tasks.home import crawl_weibo_datas
import time

# 混合
uids = [5542048577,5318963740,2801543063,2685880717,5232044091,6986509460,2900121247,6255146945,2285140023,3689223877,]

for uid in uids:
    crawl_person_infos(uid)

    crawl_weibo_datas(uid)
    time.sleep(11)


