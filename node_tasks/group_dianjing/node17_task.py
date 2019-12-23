from tasks.user import crawl_person_infos
from tasks.home import crawl_weibo_datas
import time

# 游戏
uids = [6134356306,5353688044,5353457301,5353457203,5228991532,5021981809,3967190493,3214359740,3097520421,3090995877,2852819125,2695336764,1916791032,1913374177,1888378013,1875711365,1790048444,1784000704,1781941323,1769112935,1747388557,1730967945,1719559670,1174930107,2182625882,1921993651,1850892980,2251768165,1025797561,1772625257,1884026947,1679948713,1743168193,6066063857,5541978787,5353688078,5353688077,5353688043,5353687869,5353457339,5252918579,3300194584,2910702744,2874593170,2338483575,2275106704,]

for uid in uids:
    crawl_person_infos(uid)

    crawl_weibo_datas(uid)
    time.sleep(11)

