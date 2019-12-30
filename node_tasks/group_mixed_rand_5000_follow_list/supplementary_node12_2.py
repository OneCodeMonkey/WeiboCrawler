from tasks.workers import app
from page_get.user import get_fans_or_followers_ids
from tasks.user import crawl_person_infos


uids = [1864101900,2478317574,1777683960,1779613625,1769742001,6547761261,5039555171,2026775815,2521717173,2294905875,2884262777,2545277872,6245564248,1692557183,3094377191,2712212690,1925442533,2027007763,3224586555,1829420713,1900092860,1611492585,]

# 爬取关注列表
for uid in uids:
    result = get_fans_or_followers_ids(uid,2,1)
    for user_id in result:
        crawl_person_infos(user_id)
