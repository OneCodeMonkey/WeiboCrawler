from tasks.user import crawl_person_infos
from tasks.home import crawl_weibo_datas
import time

# 混合
uids = [5052460865,3754535037,6516897834,5591257622,6631658231,5807334961,5263832199,5508232812,2647330095,5544391045,]

for uid in uids:
    crawl_person_infos(uid)

    crawl_weibo_datas(uid)
    time.sleep(11)


