from tasks.user import crawl_person_infos
from tasks.home import crawl_weibo_datas
from tasks.comment import crawl_comment_page
import time

# 情感榜 https://v6.bang.weibo.com/czv/qinggan?period=month
mids = [4430578961241391]

for mid in mids:
    crawl_comment_page(mid)

    time.sleep(11)