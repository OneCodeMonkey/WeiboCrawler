from tasks.workers import app
from page_get.user import get_fans_or_followers_ids
from tasks.user import crawl_person_infos


uids = [1769075880,2496915357,6120670057,1646006072,5682293993,1881438232,3971352181,1927722847,1931141622,2329010334,1594617517,5406329647,1766275912,2189286375,1718674155,2623531431,5416504629,6042105339,5524419632,1915039462,3596404982,6536065630,]

# 爬取关注列表
for uid in uids:
    result = get_fans_or_followers_ids(uid,2,1)
    for user_id in result:
        crawl_person_infos(user_id)
