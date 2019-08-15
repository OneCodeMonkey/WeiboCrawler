# -*- coding=UTF-8 -*-
import json
from bs4 import BeautifulSoup
from logger.log import parser
from db.models import WeiboComment
from decorators.decorator import parse_decorator


@parse_decorator('')
def get_html_cont(html):
    cont = ''
    data = json.loads(html, encoding='utf-8').get('data', '')
    if data:
        cont = data.get('html', '')

    return cont


def get_total_page(html):
    try:
        page_count = json.loads(html, encoding='UTF-8').get('data', '').get('page', '').get('totalpage', 1)
    except Exception as e:
        parser.error('获取总页面出错，原因：{}'.format(e))
        page_count = 1

    return page_count


@parse_decorator('')
def get_next_url(html):
    cont = get_html_cont(html)
    if not cont:
        return ''
    soup = BeautifulSoup(cont, 'html.parser')
    url = ''

    if 'comment_loading' in cont:
        url = soup.find(attrs={'node-type': 'comment_loading'}).get('action-data')

    if 'click_more_comment' in cont:
        url = soup.find(attrs={'action-type': 'click_more_comment'}).get('action-data')

    return url
