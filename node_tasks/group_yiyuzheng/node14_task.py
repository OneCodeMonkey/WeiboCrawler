from tasks.user import crawl_person_infos
from tasks.home import crawl_weibo_datas
import time

# 混合
uids = [5544351258,2139515142,5596162709,5132215093,7060453716,7316855630,2436946010,6052939320,6500633722,6020397377,1830690631,2656185045,6469749851,7035448202,5445233596,6642227434,6486241940,6495362348,6437615541,5594564835,]

for uid in uids:
    crawl_person_infos(uid)

    crawl_weibo_datas(uid)
    time.sleep(11)


