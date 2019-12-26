from tasks.repost import crawl_repost_page
from tasks.workers import app

app.send_task('tasks.repost.crawl_repost_page', args=(4442818895949202, 5582937157),
                      queue='repost_crawler', routing_key='repost_info')