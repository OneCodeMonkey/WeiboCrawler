from tasks.workers import app
from page_get.user import get_fans_or_followers_ids
from tasks.user import crawl_person_infos


uids = [3252495162,1308455682,2194098132,1597179222,2201801034,1410366070,1848003500,2434609484,2966156990,3574972741,6150014074,2103948912,1990937211,1789042740,7056215092,3223246051,1547711612,1706521843,1768346942,2198659273,5095933262,2710794531,]

# 爬取关注列表
for uid in uids:
    result = get_fans_or_followers_ids(uid,2,1)
    for user_id in result:
        crawl_person_infos(user_id)
