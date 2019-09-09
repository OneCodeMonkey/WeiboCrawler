from urllib import parse as url_parse

from logger import crawler
from .workers import app
from page_get import get_page
from config import get_max_search_page
from page_parse import search as parse_search
from db.dao import (KeywordsOper, KeywordsDataOper, WbDataOper)

URL = 'https://s.weibo.com/weibo?q={$topic}&typeall=1&suball=1&timescope=custom:{$startTime}:{$endTime}&Refer=g'

LIMIT = get_max_search_page() + 1


@app.task(ignore_result = True)
def search_keyword_topic(keyword, keyword_id):
    crawler.info('We are crawling weibo topic content with keyword "{}"' . format(keyword))
    cur_page = 1
    encode_keyword = url_parse.quote(keyword)
    while cur_page < LIMIT:
        cur_url = URL.format(encode_keyword, cur_page)
        search_page = get_page(cur_url, auth_level=2)
        if not search_page:
            crawler.info('No such result for keyword {}, the source page is {}' . format(keyword, search_page))
            return

        search_list = parse_search.get_search_info(search_page)
        if cur_page == 1:
            cur_page += 1
        elif 'noresult tit' not in search_page:
            cur_page += 1
        else:
            crawler.info('Keyword {} has been crawled in this turn' . format(keyword))
            return

        for wb_data in search_list:
            rs = WbDataOper.get_wb_by_mid(wb_data.weibo_id)
            KeywordsDataOper.insert_keyword_wbid(keyword_id, wb_data.weibo_id)
            if rs:
                crawler.info('Weibo {} has been crawled, skip it.' . format(wb_data.weibo_id))
                continue
            else:
                WbDataOper.add_one(wb_data)
                app.send_task('tasks.user.crawl_person_infos', args=(wb_data.uid,), queue='user_crawler', routing_key='for_user_info')


@app.task(ignore_result = True)
def execute_topic_task():
    keywords = KeywordsOper.get_search_keywords()
    for each in keywords:
        app.send_task('tasks.topic.search_keyword_topic', args=(each[0], each[1]), queue='topic_crawler',
                      routing_key='topic_info')



