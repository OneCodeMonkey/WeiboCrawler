# -*- coding=UTF-8 -*-
import time
import random
from tasks.comment import crawl_comment_page
from db.models import WeiboData
from db.basic import db_session
from logger import crawler


results = db_session.query(WeiboData).filter(WeiboData.weibo_cont.like("%晚安短信计划%")).limit(4200).offset(4200 * 2).all()

count = 0;
for item in results:
    mid = item.weibo_id
    count += 1
    crawler.info("crawling comment of weiboid:" + str(mid) + "--count:" + str(count))
    crawl_comment_page(mid)
    time.sleep(random.randint(1, 4))
