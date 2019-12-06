from tasks.user import crawl_person_infos
from tasks.home import crawl_weibo_datas
import time

# 混合
uids = [6058924373,6086250040,5279892299,5719912765,2562886023,5835858491,5371066216,6933061155,3477063211,2424270232,5975205298,3225347261,5669545330,7296939506,5296619183,7234232781,7176240060,6646497197,5421504171,5567716815,]

for uid in uids:
    crawl_person_infos(uid)

    crawl_weibo_datas(uid)
    time.sleep(11)


