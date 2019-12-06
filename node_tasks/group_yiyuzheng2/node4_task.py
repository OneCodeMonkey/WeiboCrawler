from tasks.user import crawl_person_infos
from tasks.home import crawl_weibo_datas
import time

# 混合
uids = [6363455352,2032498521,5656306681,3289211211,5890278783,2927264063,5847391111,3880788101,7307739092,6191097146,]

for uid in uids:
    crawl_person_infos(uid)

    crawl_weibo_datas(uid)
    time.sleep(11)


