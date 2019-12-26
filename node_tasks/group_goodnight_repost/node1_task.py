from tasks.repost import crawl_repost_page
from tasks.workers import app

app.send_task('tasks.repost.crawl_repost_page', args=(4442622422300558, 1197191492),
                      queue='repost_crawler', routing_key='repost_info')