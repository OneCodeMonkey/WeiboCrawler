from tasks.user import crawl_person_infos
from tasks.home import crawl_weibo_datas
import time

# 设计师
uids = [3515906527,5053585912,1794263067,5723050605,2087618051,2095941851,7070902463,6202834863,2176934627,2322360802,3153364515,6391284359,6220479532,6073307618,3470569750,2912166957,]

for uid in uids:
    crawl_person_infos(uid)

    crawl_weibo_datas(uid)
    time.sleep(11)


