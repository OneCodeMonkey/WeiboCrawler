from tasks.workers import app
from page_get.user import get_fans_or_followers_ids

uids = [1971239183]

# 爬取关注列表
for uid in uids:
    result = get_fans_or_followers_ids(uid,2,1)
    for user_id in result:
        app.send_task('tasks.user.crawl_person_infos', args=(user_id,), queue='user_crawler',
                      routing_key='for_user_info')
