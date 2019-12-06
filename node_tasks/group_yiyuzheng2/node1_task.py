from tasks.user import crawl_person_infos
from tasks.home import crawl_weibo_datas
import time

# 混合
uids = [5715039455,5941946076,6073258124,1978796675,1787104434,6405397541,7121394152,5578071748,5658471372,1950843557,]

for uid in uids:
    crawl_person_infos(uid)

    crawl_weibo_datas(uid)
    time.sleep(11)


