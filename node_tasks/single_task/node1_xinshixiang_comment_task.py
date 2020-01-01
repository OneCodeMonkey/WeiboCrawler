from tasks.comment import crawl_comment_page
import time

mids = [4455991410414032]

for mid in mids:
    crawl_comment_page(mid)
    time.sleep(11)