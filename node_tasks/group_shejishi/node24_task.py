from tasks.user import crawl_person_infos
from tasks.home import crawl_weibo_datas
import time

# 设计师
uids = [2161791955,6399689363,2187357511,6188561345,2881597630,5938119686,2481102270,2355366595,5359507718,5419169627,6419952113,2334467995,2161137340,5043830622,6001193414,2784926354,]

for uid in uids:
    crawl_person_infos(uid)

    crawl_weibo_datas(uid)
    time.sleep(11)


