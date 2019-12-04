from tasks.user import crawl_person_infos
from tasks.home import crawl_weibo_datas
import time

# 游戏
uids = [5917763899,2723025201,5910222230,6429986361,6367247422,6283772284,6100007012,6085976280,5761018481,3165213811,2721885803,7318708217,7293785888,6787487694,3972904674,6666157473,7029341518,6245174985,2238068383,2843862092,5027299527,6560148225,5718312295,3867411829,1954214947,5398774354,3035421633,2277072351,5985651387,2791212092,7317646021,6519121673,6026562979,3477305321,5846274792,3955909237,6553348810,6053233047,5037230274,2780052373,2384889987,3748710397,6804996687,5933376146,2310116293,2830453473,]

for uid in uids:
    crawl_person_infos(uid)

    crawl_weibo_datas(uid)
    time.sleep(11)


