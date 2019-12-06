from tasks.user import crawl_person_infos
from tasks.home import crawl_weibo_datas
import time

# 混合
uids = [7033376297,6122472851,5871953072,3200291613,3645246764,5422362078,2719341377,3803714488,5458514600,6820705802,]

for uid in uids:
    crawl_person_infos(uid)

    crawl_weibo_datas(uid)
    time.sleep(11)


