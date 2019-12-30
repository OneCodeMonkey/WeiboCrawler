from tasks.workers import app
from page_get.user import get_fans_or_followers_ids
from tasks.user import crawl_person_infos


uids = [6971438529,3847200576,1727587894,1822820195,5023694916,6994706348,1906878860,2572418522,1750446441,3252419550,2429142192,2724411022,1268226757,5157326121,3582228124,2079950103,5721334082,6414242568,2487583840,2716292897,1874261253,2423763501,]

# 爬取关注列表
for uid in uids:
    result = get_fans_or_followers_ids(uid,2,1)
    for user_id in result:
        crawl_person_infos(user_id)
