from tasks.user import crawl_person_infos
from tasks.home import crawl_weibo_datas
import time

# 情感榜 https://v6.bang.weibo.com/czv/qinggan?period=month
uids = [2678630280]

for uid in uids:
    crawl_person_infos(uid)

    crawl_weibo_datas(uid)
    time.sleep(11)