from tasks.user import crawl_person_infos
from tasks.home import crawl_weibo_datas
import time

# 混合
uids = [5043600511,1201195972,1789069994,5098354132,1876565231,5720666027,3342163294,3284306205,5492755954,1109752587,]

for uid in uids:
    crawl_person_infos(uid)

    crawl_weibo_datas(uid)
    time.sleep(11)


