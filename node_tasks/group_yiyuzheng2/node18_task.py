from tasks.user import crawl_person_infos
from tasks.home import crawl_weibo_datas
import time

# 混合
uids = [6185106414,6389958272,5491428565,5629802140,2703137480,2173551142,6538761950,5441684145,5512492499,5266781491,]

for uid in uids:
    crawl_person_infos(uid)

    crawl_weibo_datas(uid)
    time.sleep(11)


