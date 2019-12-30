from tasks.workers import app
from page_get.user import get_fans_or_followers_ids
from tasks.user import crawl_person_infos


uids = [6070807880,1945139410,1780799373,1989122377,1688150265,2005157901,6382699228,1651067270,1764798902,1748874275,1615576114,1697442011,2688392621,2259817395,]

# 爬取关注列表
for uid in uids:
    result = get_fans_or_followers_ids(uid,2,1)
    for user_id in result:
        crawl_person_infos(user_id)
