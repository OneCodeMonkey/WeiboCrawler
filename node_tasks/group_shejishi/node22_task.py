from tasks.user import crawl_person_infos
from tasks.home import crawl_weibo_datas
import time

# 设计师
uids = [5958124866,1937381685,6399689363,6188561345,5938119686,5419169627,2161137340,5043830622,6001193414,5985871120,1812466714,5559994421,5780295881,5132252647,3019419633,2375835397,]

for uid in uids:
    crawl_person_infos(uid)

    crawl_weibo_datas(uid)
    time.sleep(11)


