# -*- coding=UTF-8 -*-
import time
from tasks.comment import crawl_comment_page

mids = [4430578961241391,]

for mid in mids:
    crawl_comment_page(mid)
    time.sleep(3)
