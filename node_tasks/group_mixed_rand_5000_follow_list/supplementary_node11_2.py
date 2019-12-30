from tasks.workers import app
from page_get.user import get_fans_or_followers_ids
from tasks.user import crawl_person_infos


uids = [5593257190,2673554493,1775679527,1982235770,1869621411,1777288500,2113868664,1887141912,3924590924,3179639553,1847402263,7212231597,1922043173,1728659973,2894051794,2071687225,1761488870,5254050144,1819882553,2529912044,5833731776,1570311561,]

# 爬取关注列表
for uid in uids:
    result = get_fans_or_followers_ids(uid,2,1)
    for user_id in result:
        crawl_person_infos(user_id)
