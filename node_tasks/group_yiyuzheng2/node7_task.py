from tasks.user import crawl_person_infos
from tasks.home import crawl_weibo_datas
import time

# 混合
uids = [5392702553,6091399070,1715262511,6280932085,5655544793,3287590481,6374130098,5415008084,3968221022,3028235255,]

for uid in uids:
    crawl_person_infos(uid)

    crawl_weibo_datas(uid)
    time.sleep(11)


