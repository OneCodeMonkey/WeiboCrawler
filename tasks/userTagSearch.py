from urllib import parse as url_parse
from logger import crawler
from .workers import app
from page_get import get_page
from config import get_max_search_page
from page_parse import userTagSearch as parse_user_tag_search
from db.dao import(UserOper, WbDataOper)

URL = 'https://s.weibo.com/user/&tag={}&page={}'

LIMIT = get_max_search_page() + 1

@app.task(ignore_result = True)
def search_user_tag_list(tag):
    crawler.info('we are crawling weibo user tag search with tag "{}"' . format(tag))
    cur_page = 1
    tag = url_parse.quote(tag)
    while cur_page < LIMIT:
        cur_url = URL.format(tag, cur_page)
        search_page = get_page(cur_url, auth_level=2)
        if not search_page:
            crawler.info('No such result for tag {}, the source page is {}' . format(tag, search_page))
            return

        search_list = parse_user_tag_search.get_user_tag_search_info(search_page)
        if cur_page == 1:
            cur_page += 1
        elif '抱歉，未找到' not in search_page:
            cur_page += 1
        else:
            crawler.info('tag {} has been crawled in this turn' . format(tag))
            return

        crawler.info("search_list" + "&&" . join(search_list))

@app.task(ignore_result = True)
def execute_search_user_tag_task():
    keywords = []
    # for item in keywords:
    #     app.send_task('tasks.userTagSearch.')