# -*- coding=UTF-8 -*-
import time
import random
from tasks.comment import crawl_comment_page
from db.models import WeiboData
from db.basic import db_session
from logger import crawler


mids = db_session.query(WeiboData).filter(WeiboData.weibo_cont.like("%晚安短信计划%")).limit(10).all()

for mid in mids:
    crawler.info("crawling comment of weiboid:" + mid.weibo_id)
    crawl_comment_page(mid)
    time.sleep(random.randint(1, 4))
