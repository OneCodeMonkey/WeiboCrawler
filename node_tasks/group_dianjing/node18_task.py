from tasks.user import crawl_person_infos
from tasks.home import crawl_weibo_datas
import time

# 游戏
uids = [2199232411,1983369493,2199232411,1983369493,1974948370,1954446492,1947234603,1935680255,1908008931,1896452053,1891043677,1870906483,1798014297,1773321944,1735759654,1715347460,1703586773,1690614447,1678513070,1667717970,1637290141,1633809542,1224689101,1153976282,1093979465,2641204937,1792940074,1914206157,1731316987,2500397143,1727025627,2265106971,2553129774,1358254911,5556070375,5886704962,5582034632,5353688555,5209163893,2755961661,2612819781,1998747164,1174399645,1007494353,1768961335,6012423726,]

for uid in uids:
    crawl_person_infos(uid)

    crawl_weibo_datas(uid)
    time.sleep(11)


