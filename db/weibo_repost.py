# -*- coding=UTF-8 -*-
from db.basic_db import db_session
from db.models import WeiboRepost
from decorators.decorator import db_commit_decorator


# 有一个异常未找到原因：pymysql.err.IntegrityError
@db_commit_decorator
def save_reposts(repost_list):
    for repost in repost_list:
        r = get_repost_by_rid(repost.weibo_id)
        if not r:
            save_reposts(repost)
    db_session.commit()


@db_commit_decorator
def save_repost(repost):
    db_session.add(repost)
    db_session.commit()


def get_repost_by_rid(rid):
    return db_session.query(WeiboRepost).filter(WeiboRepost.weibo_id == rid).first()
