# -*- coding=UTF-8 -*-
import time
from tasks.comment import crawl_comment_page
from db.models import WeiboData
from db.basic import db_session
from logger import crawler


mids = db_session.query(WeiboData).filter(WeiboData.weibo_cont.like("%晚安短信计划%")).all().limit(10)

for mid in mids:
    crawler.info(mid.weibo_id + "--item")
