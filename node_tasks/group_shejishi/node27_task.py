from tasks.user import crawl_person_infos
from tasks.home import crawl_weibo_datas
import time

# 设计师
uids = [6508329500,5865911542,5805694404,5794890532,5726546925,5627730081,5514281329,2073480692,1918798500,1760484052,2493502114,5462381110,5363827230,6514871739,6507813324,6481085740,]

for uid in uids:
    crawl_person_infos(uid)

    crawl_weibo_datas(uid)
    time.sleep(11)


