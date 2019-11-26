from tasks.user import crawl_person_infos
from tasks.home import crawl_weibo_datas
import time

# 设计师
uids = [5960782103,6043741812,5982549329,2876410994,5436655630,2400956902,6681428580,6305344918,5794648001,5165436750,3717595473,2509053865,2759880741,3050694811,6077396468,6052973113,]

for uid in uids:
    crawl_person_infos(uid)

    crawl_weibo_datas(uid)
    time.sleep(11)


