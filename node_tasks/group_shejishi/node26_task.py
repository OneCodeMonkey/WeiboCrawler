from tasks.user import crawl_person_infos
from tasks.home import crawl_weibo_datas
import time

# 设计师
uids = [6001789281,2294946357,2483065630,2298280353,6389820422,2877523477,5317522123,3229277993,5516255403,2246416295,5998182049,5041992103,3173759005,5589772837,6567432164,6534592163,]

for uid in uids:
    crawl_person_infos(uid)

    crawl_weibo_datas(uid)
    time.sleep(11)


