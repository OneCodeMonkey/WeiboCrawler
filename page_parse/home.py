# -*- coding=UTF-8 -*-
import re,json,urllib.parse
from bs4 import BeautifulSoup
from page_get import status
from logger.log import parser
from db.models import WeiboData
from config.conf import get_crawling_mode
from decorators.decorator import parse_decorator

ORIGIN = 'http'
PROTOCOL = 'https'
ROOT_URL = 'weibo.com'
CRAWLING_MODE = get_crawling_mode()


@parse_decorator('')
def get_weibo_infos_right(html):
    soup = BeautifulSoup(html, 'html.parser')
    scripts = soup.find_all('script')
    pattern = re.compile(r'FM.view\((.*)\)')

    cont = ''
    for script in scripts:
        m = pattern.search(script.string)
        if m and 'fl_menu' in script.string:
            all_info = m.group(1)
            cont += json.loads(all_info).get('html', '')

    return cont


@parse_decorator(5)
def get_weibo_info_detail(each, html):
    wb_data = WeiboData()
    user_cont = each.find(attrs={'class': 'face'})
    user_info = str(user_cont.find('a'))
    user_pattern = 'id=(\\d+)&amp'
    m = re.search(user_pattern, user_info)

    if m:
        wb_data.uid = m.group(1)
    else:
        parser.warning("fail to get user's id, the page source is {}".format(html))
        return None

    weibo_pattern = 'mid=(\\d+)'
    m = re.search(weibo_pattern, str(each))
    if m:
        wb_data.weibo_id = m.group(1)
    else:
        parser.warning("fail to get weibo's id, the page source: {}".format(html))
        return None

    time_url = each.find(attrs={'node-type': 'feed_list_item_date'})
    wb_data.create_time = time_url.get('title', '')
    wb_data.weibo_url = time_url.get('href', '')
    if ROOT_URL not in wb_data.weibo_url:
        wb_data.weibo_url = '{}://{}{}'.format(PROTOCOL, ROOT_URL, wb_data.weibo_url)

    def url_filter(url):
        return ':'.join([PROTOCOL, url]) if PROTOCOL not in url and ORIGIN not in url else url

    try:
        imgs = str(each.find(attrs={'node-type': 'feed_content'}).find(attrs={'node-type': 'feed_list_media_prev'}).find_all('img'))
        imgs_url = map(url_filter, re.findall(r"src=\"(.+?)\"", imgs))
        wb_data.weibo_img = ';'.join(imgs_url)
    except Exception:
        wb_data.weibo_img = ''

    try:
        li = str(each.find(attrs={'node-type': 'feed_content'}).find(attrs={'node-type': 'feed_list_media_prev'}).find_all('li'))
        extracted_url = urllib.parse.unquote(re.findall(r"video_src=(.+?)&amp;", li)[0])
        wb_data.weibo_video = url_filter(extracted_url)
    except Exception:
        wb_data.weibo_video = ''

    try:
        wb_data.weibo_cont = each.find(attrs={'node-type': 'feed_content'}).find(attrs={'node-type': 'feed_list_content'}).text.strip()
    except Exception:
        wb_data.weibo_cont = ''

    if '展开全文' in str(each):
        is_all_cont = 0
    else:
        is_all_cont = 1

    try:
        wb_data.device = each.find(attrs={'class': 'WB_from S_txt2'}).find(attrs={'action-type': 'app_source'}).text
    except Exception:
        wb_data.device = ''

    try:
        wb_data.repost_num = int(each.find(attrs={'action-type': 'fl_forward'}).find_all('em')[1].text)
    except Exception:
        wb_data.repost_num = 0

    try:
        wb_data.comment_num = int(each.find(attrs={'action-type': 'fl_comment'}).find_all('em')[1].text)
    except Exception:
        wb_data.comment_num = 0

    try:
        wb_data.praise_num = int(each.find(attrs={'action-type': 'fl_like'}).find_all('em')[1].text)
    except Exception:
        wb_data.praise_num = 0

    return wb_data, is_all_cont


def get_weibo_list(html):
    if not html:
        return list()
    soup = BeautifulSoup(html, "html.parser")
    feed_list = soup.find_all(attrs={'action-type': 'feed_list_item'})
    weibo_datas = []
    for data in feed_list:
        r = get_weibo_info_detail(data, html)
        if r is not None:
            wb_data = r[0]
            if r[1] == 0 and CRAWLING_MODE == 'accurate':
                weibo_cont = status.get_cont_of_weibo(wb_data.weibo_id)
                wb_data.weibo_cont = weibo_cont if weibo_cont else wb_data.weibo_cont
            weibo_datas.append(wb_data)

    return weibo_datas


def get_max_num(html):
    soup = BeautifulSoup(html, "html.parser")
    href_list = soup.find(attrs={'action-type': 'feed_list_page_morelist'}).find_all('a')
    return len(href_list)


def get_wbdata_fromweb(html):
    cont = get_weibo_infos_right(html)
    return get_weibo_list(cont)


def get_home_wbdata_byajax(html):
    cont = json.loads(html, encoding='UTF-8').get('data', '')
    return get_weibo_list(cont)


def get_total_page(html):
    cont = json.loads(html, encoding='UTF-8').get('data', '')
    if not cont:
        return 1
    return get_max_num(cont)
