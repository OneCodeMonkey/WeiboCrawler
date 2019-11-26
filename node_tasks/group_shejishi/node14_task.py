from tasks.user import crawl_person_infos
from tasks.home import crawl_weibo_datas
import time

# 设计师
uids = [2497016600,5087394184,1849921530,1784200667,5379706773,2074098875,3058993777,1219930752,2153557273,1909052412,3675602030,1245992822,1242504281,1971072683,2112863224,6885112218,]

for uid in uids:
    crawl_person_infos(uid)

    crawl_weibo_datas(uid)
    time.sleep(11)


