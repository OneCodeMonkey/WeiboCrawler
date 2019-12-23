from tasks.user import crawl_person_infos
from tasks.home import crawl_weibo_datas
import time

# 游戏
uids = [6152975337,6055170552,5658263904,5193211120,5079836205,3877471993,3562028234,3393530974,1985441664,1725146391,1949298097,5442046075,3471453370,5292681150,3796562175,5737574832,1985153130,2099477137,7317138977,7274512142,6888081308,6578818153,6468214141,6032476736,5868246292,5251312101,2990558463,2622050322,1594372587,5868292041,3106576924,2758513297,5972139913,5246451769,5216341459,7010084604,6694921505,6309937661,6213064122,6076338698,5905952710,5867808585,5851882558,5794014327,5679583673,5533083701,]

for uid in uids:
    crawl_person_infos(uid)

    crawl_weibo_datas(uid)
    time.sleep(11)

