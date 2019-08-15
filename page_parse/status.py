# -*- coding=UTF-8 -*-
# 微博详情页
import re,json
from bs4 import BeautifulSoup
from decorators.decorator import parse_decorator
from logger.log import parser


@parse_decorator('')
def get_userid(html):
    pattern = re.compile(r'\$CONFIG\[\'oid\'\]=\'(.*)\';')
    m = pattern.search(html)
    return m.group(1) if m else ''


@parse_decorator('')
def get_username(html):
    pattern = re.compile(r'\$CONFIG\[\'onick\'\]=\'(.*)\';')
    m = pattern.search(html)
    return m.group(1) if m else ''


@parse_decorator('')
def get_userdomain(html):
    pattern = re.compile(r'\$CONFIG\[\'domain\'\]=\'(.*)\';')
    m = pattern.search(html)
    return m.group(1) if m else ''


@parse_decorator('')
def _get_statushtml(html):
    soup = BeautifulSoup(html, "html.parser")
    scripts = soup.find_all('script')
    pattern = re.compile(r'FM.view\((.*)\)')
    cont = ''
    for script in scripts:
        try:
            m = pattern.search(script.string)
            if m and 'pl.content.weiboDetail.index' in script.string:
                all_info = m.group(1)
                # TODO 留意这里可能有未处理的异常
                cont = json.loads(all_info)['html']
        except TypeError:
            return ''
        except Exception as e:
            parser.error('__get_statushtml()错误，具体错误是：{e}'.format(e=e))
            parser.error('网页代码为{page}'.format(page=html))

    return cont


@parse_decorator('')
def get_mid(html):
    cont = _get_statushtml(html)
    soup = BeautifulSoup(cont, 'html.parser')
    try:
        return soup.find(attrs={'action-type': 'feed_list_item'})['mid']
    except TypeError:
        mid_pattern = r'mid=(\d+)'
        mid_matcher = re.search(mid_pattern, html)
        return mid_matcher.group(1) if mid_matcher else ''
    except Exception as e:
        parser.error('get_mid() 发生异常，具体为{e}'.format(e=e))


@parse_decorator('')
def get_originalmid(html):
    if is_not(html):
        return get_mid(html)
    else:
        cont = _get_statushtml(html)
        soup = BeautifulSoup(cont, 'html.parser')
        return soup.find(attrs={'action-type': 'feed_list_item'})['omid']


@parse_decorator('')
def get_statussource(html):
    cont = _get_statushtml(html)
    soup = BeautifulSoup(cont, 'html.parser')
    try:
        return soup.find(attrs={'action-type':'app_source'}).text
    except AttributeError:
        try:
            return soup.find(attrs={'class': 'WB_from S_txt2'}).find_all('a')[1].text
        except Exception:
            return ''

