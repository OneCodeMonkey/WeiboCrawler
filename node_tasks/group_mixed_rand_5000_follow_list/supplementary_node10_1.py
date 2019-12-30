from tasks.workers import app
from page_get.user import get_fans_or_followers_ids
from tasks.user import crawl_person_infos


uids = [1563015661,1798407722,1874590182,2344538900,1763599943,3048369783,2096036471,1401638893,5100227686,2649817191,2748322693,2401787223,1928228151,2312774902,2786753782,2594219392,2653545087,3262721871,5605014126,2114776732,1639313642,1312400911,]

# 爬取关注列表
for uid in uids:
    result = get_fans_or_followers_ids(uid,2,1)
    for user_id in result:
        crawl_person_infos(user_id)
