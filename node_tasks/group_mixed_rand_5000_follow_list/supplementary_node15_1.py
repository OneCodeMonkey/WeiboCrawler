from tasks.workers import app
from page_get.user import get_fans_or_followers_ids
from tasks.user import crawl_person_infos


uids = [1593577594,2996730025,1271666612,2845101943,2034781974,6444317745,1687367547,2083250041,1795153485,2920770290,5466017088,1853172161,2796853997,3639873840,]

# 爬取关注列表
for uid in uids:
    result = get_fans_or_followers_ids(uid,2,1)
    for user_id in result:
        crawl_person_infos(user_id)
