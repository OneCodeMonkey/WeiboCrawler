import json
from .workers import app
from page_parse import comment
from config import conf
from page_get import get_page
from db.dao import (
    WbDataOper, CommentOper)
from logger import crawler
from celery.exceptions import SoftTimeLimitExceeded
import time

BASE_URL = 'http://weibo.com/aj/v6/comment/big?ajwvr=6&id={}&page={}'


@app.task(ignore_result=True)
def crawl_comment_by_page(mid, page_num):
    try:
        cur_url = BASE_URL.format(mid, page_num)
        html = get_page(cur_url, auth_level=1, is_ajax=True)
        comment_datas = comment.get_comment_list(html, mid)
    except SoftTimeLimitExceeded:
        crawler.error(
            "comment SoftTimeLimitExceeded    mid={mid} page_num={page_num}".
            format(mid=mid, page_num=page_num))
        app.send_task(
            'tasks.comment.crawl_comment_by_page',
            args=(mid, page_num),
            queue='comment_page_crawler',
            routing_key='comment_page_info')
    CommentOper.add_all(comment_datas)
    if page_num == 1:
        WbDataOper.set_weibo_comment_crawled(mid)

    if not comment_datas:
        crawler.info("comment list empty!")
    for i in comment_datas:
        crawler.info("--comment item")

    return html, comment_datas


@app.task(ignore_result=True)
def crawl_comment_page(mid):
    limit = conf.get_max_comment_page() + 1
    first_page = crawl_comment_by_page(mid, 1)[0]
    crawler.info("--first_page")
    total_page = comment.get_total_page(first_page)
    crawler.info(str(total_page) + "--total_page")

    if total_page < limit:
        limit = total_page + 1

    for page_num in range(2, limit):
        crawl_comment_by_page(mid, page_num)
        time.sleep(3)


@app.task(ignore_result=True)
def execute_comment_task():
    weibo_datas = WbDataOper.get_weibo_comment_not_crawled()
    for weibo_data in weibo_datas:
        app.send_task('tasks.comment.crawl_comment_page', args=(weibo_data.weibo_id,), queue='comment_crawler',
                      routing_key='comment_info')
