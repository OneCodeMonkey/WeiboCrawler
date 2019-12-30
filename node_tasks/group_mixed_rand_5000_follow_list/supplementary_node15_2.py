from tasks.workers import app
from page_get.user import get_fans_or_followers_ids
from tasks.user import crawl_person_infos


uids = [3175031813,1892760563,5522484119,6519121673,2432174463,1898472870,1942110463,3064856317,1082960433,3909375213,1314901714,1920185011,3694583332,1170472592,]

# 爬取关注列表
for uid in uids:
    result = get_fans_or_followers_ids(uid,2,1)
    for user_id in result:
        crawl_person_infos(user_id)
