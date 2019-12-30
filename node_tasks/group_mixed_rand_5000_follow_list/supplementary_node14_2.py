from tasks.workers import app
from page_get.user import get_fans_or_followers_ids
from tasks.user import crawl_person_infos


uids = [1741419277,3262542124,2704825117,6030182039,2949504577,2719698392,1943910207,2191344287,1910716662,2676742562,1393242232,1836955377,5894940394,5118118701,]

# 爬取关注列表
for uid in uids:
    result = get_fans_or_followers_ids(uid,2,1)
    for user_id in result:
        crawl_person_infos(user_id)
