from urllib import parse as url_parse

from logger import crawler
from .workers import app
from page_get import get_page
from config import get_max_search_page
from page_parse import topic as parse_topic
from db.dao import (KeywordsOper, KeywordsDataOper, WbDataOper)

# url示例 http://s.weibo.com/weibo?q={}&nodup=1&&timescope=custom:2019-09-09-0:2019-09-09-12&page={}
URL = 'http://s.weibo.com/weibo?q={}&nodup=1&&timescope=custom:{}:{}&page={}'

LIMIT = get_max_search_page() + 1


@app.task(ignore_result = True)
def search_keyword_topic(keyword, keyword_id, start_time='', end_time=''):
    crawler.info('We are crawling weibo topic content with keyword "{}"' . format(keyword))
    cur_page = 1
    encode_keyword = url_parse.quote(keyword)
    while cur_page < LIMIT:
        cur_url = URL.format(encode_keyword, start_time, end_time, cur_page)
        search_page = get_page(cur_url, auth_level=2)
        if not search_page:
            crawler.info('No such result for keyword {}, the source page is {}' . format(keyword, search_page))
            return

        search_list = parse_topic.get_search_info(search_page)
        if cur_page == 1:
            cur_page += 1
        elif '您可以尝试更换关键词' not in search_page:
            cur_page += 1
        else:
            crawler.info('Keyword {} has been crawled in this turn' . format(keyword))
            return

        for wb_data in search_list:
            # rs = WbDataOper.get_wb_by_mid(wb_data.weibo_id)
            KeywordsDataOper.insert_keyword_wbid(keyword_id, wb_data.weibo_id)
            # if rs:
            #     crawler.info('Weibo {} has been crawled, skip it.' . format(wb_data.weibo_id))
            #     continue
            # else:
            WbDataOper.add_one(wb_data)
            try:
                app.send_task('tasks.user.crawl_person_infos', args=(wb_data.uid,), queue='user_crawler', routing_key='for_user_info')
            except Exception as e:
                crawler("topic send user_crawler task error, reason is:" . e)



@app.task(ignore_result = True)
def execute_topic_task():
    keywords = KeywordsOper.get_search_keywords()
    for each in keywords:
        app.send_task('tasks.topic.search_keyword_topic', args=(each[0], each[1]), queue='topic_crawler',
                      routing_key='topic_info')



