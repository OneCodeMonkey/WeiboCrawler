from tasks.user import crawl_person_infos
from tasks.home import crawl_weibo_datas
import time

# 混合
uids = [5413407530,5643356496,3176741452,5692001607,6286130982,6408424712,5062632473,5993306913,6397711075,5711172909,]

for uid in uids:
    crawl_person_infos(uid)

    crawl_weibo_datas(uid)
    time.sleep(11)


