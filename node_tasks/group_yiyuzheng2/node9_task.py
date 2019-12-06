from tasks.user import crawl_person_infos
from tasks.home import crawl_weibo_datas
import time

# 混合
uids = [2274895227,5811136688,6114792181,2622305565,3868943557,3567407063,5877851793,5664356301,5231976262,6104013265,]

for uid in uids:
    crawl_person_infos(uid)

    crawl_weibo_datas(uid)
    time.sleep(11)


