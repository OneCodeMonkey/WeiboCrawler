from tasks.user import crawl_person_infos
from tasks.home import crawl_weibo_datas
import time

# 设计师
uids = [5726360328,5099141775,3920737711,3441713892,3020402433,2121826402,1607690943,1872615163,1765625545,1605159971,3664482173,3534537807,3519636495,3314190957,3141805791,2690754270,]

for uid in uids:
    crawl_person_infos(uid)

    crawl_weibo_datas(uid)
    time.sleep(11)


