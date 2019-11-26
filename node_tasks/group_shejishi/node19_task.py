from tasks.user import crawl_person_infos
from tasks.home import crawl_weibo_datas
import time

# 设计师
uids = [2102898974,5141635898,2151485881,3483662410,1569288802,5695484661,2732315725,2663012551,3901549474,3540651234,5522484119,1906904747,5382618347,2487177671,1899841331,3558248344,]

for uid in uids:
    crawl_person_infos(uid)

    crawl_weibo_datas(uid)
    time.sleep(11)


