from tasks.user import crawl_person_infos
from tasks.home import crawl_weibo_datas
import time

# 设计师
uids = [3558248344,2994673875,6854011249,5797834881,5528654701,2027895057,3911354673,5083516199,2928062717,2830543731,5770765700,5203199866,2361348251,5842614109,1740214497,2606639431,]

for uid in uids:
    crawl_person_infos(uid)

    crawl_weibo_datas(uid)
    time.sleep(11)


