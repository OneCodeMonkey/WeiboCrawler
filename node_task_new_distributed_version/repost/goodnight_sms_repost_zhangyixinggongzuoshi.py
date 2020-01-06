import sys
import os
o_path = os.getcwd() # 返回当前工作目录
sys.path.append(o_path) # 添加自己指定的搜索路径

from logger import crawler
from tasks.workers import app
from db.basic import db_session
from db.models import WeiboRepost
from sqlalchemy import and_

# recording uid, avoid repeating task
source_weibo_id = 4442818895949202      # 源微博的weibo_id
source_user_id = 5582937157     # 源微博的user_id
scrapyed = []
unscrapyed = []
unqueryedUid = []       # for parent_user_id query
queryedUidFromScrapyed = []     # for parent_user_id query

# 第一遍爬取
# app.send_task('tasks.repost.crawl_repost_page', args=(source_weibo_id, source_user_id), queue='repost_crawler', routing_key='repost_info')

# 循环遍历次级转发
maxRecursiveTimes = 100     # 最大循环次数，此为经验值，可根据实际需要调整
count = 0
while count < maxRecursiveTimes:
    result = db_session.query(WeiboRepost.weibo_id, WeiboRepost.user_id).filter(WeiboRepost.root_weibo_id == source_weibo_id).all()
    for each in result:
        checkStr = str(each[0]) + ';' + str(each[1])
        if checkStr not in scrapyed:
            unscrapyed.append(str(each[0]) + ';' + str(each[1]))
        if each[1] not in queryedUidFromScrapyed:
            unqueryedUid.append(each[1])   # 下一级，用 root_weibo_id = each[0] 的条件再查
    crawler.info("repost step1 finished, loop is:" + str(count))

    for item in unscrapyed:
        weibo_id = item.split(';')[0]
        user_id = item.split(';')[1]
        app.send_task('tasks.repost.crawl_repost_page', args=(weibo_id, user_id), queue='repost_crawler', routing_key='repost_info')    # 次级爬取
        unscrapyed.remove(item)
        scrapyed.append(item)

    crawler.info("repost step2 finished, loop is:" + str(count))

    for item in unqueryedUid:
        result2 = db_session.query(WeiboRepost.weibo_id, WeiboRepost.user_id).filter(and_(WeiboRepost.root_weibo_id == source_weibo_id, WeiboRepost.parent_user_id == int(item))).all()
        unqueryedUid.remove(item)
        queryedUidFromScrapyed.append(item)
        for each in result2:
            checkStr = str(each[0]) + ';' + str(each[1])
            if checkStr not in scrapyed:
                unscrapyed.append(str(each[0]) + ';' + str(each[1]))
            if each[1] not in queryedUidFromScrapyed:
                unqueryedUid.append(each[1])  # 下一级，用 root_weibo_id = each[0] 的条件再查

    count += 1
    crawler.info("repost step3 finished, loop is:" + str(count))