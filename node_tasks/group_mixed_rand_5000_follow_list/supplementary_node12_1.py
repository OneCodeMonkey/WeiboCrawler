from tasks.workers import app
from page_get.user import get_fans_or_followers_ids
from tasks.user import crawl_person_infos


uids = [1675577251,1933422755,1866582284,1759022583,5120801161,1807802053,2970738537,3733342060,1678185895,1739893912,1867542444,1732251151,2331821900,3883106777,5857997063,3323218494,1202586970,6618854279,1749651585,1175716264,2427411684,1776892251,]

# 爬取关注列表
for uid in uids:
    result = get_fans_or_followers_ids(uid,2,1)
    for user_id in result:
        crawl_person_infos(user_id)
