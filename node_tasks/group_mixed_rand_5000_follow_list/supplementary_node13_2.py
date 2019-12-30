from tasks.workers import app
from page_get.user import get_fans_or_followers_ids
from tasks.user import crawl_person_infos


uids = [1729853157,1971071013,6600797452,3927310323,3883057197,1237657334,1652527364,2153763780,6519195520,2589397465,1443547131,2383241937,5999249677,2353883047,6292338742,3742141357,2162330802,1390316000,2702343122,3034437500,1831626537,2420541503,]

# 爬取关注列表
for uid in uids:
    result = get_fans_or_followers_ids(uid,2,1)
    for user_id in result:
        crawl_person_infos(user_id)
