import sys
import os
import time
o_path = os.getcwd() # 返回当前工作目录
sys.path.append(o_path) # 添加自己指定的搜索路径

from logger import crawler
from tasks.user import crawl_person_infos
from tasks.workers import app

uids = [
    1895394815,
    1676424404,
    2729129850,
    2129452154,
    5920389143,
    6114793827,
    1142553484,
    2203132141,
    2769301163,
    5949578941,
    1791900893,
    2429640182,
    2288691440,
    6077989896,
    1699540307,
    6498676117,
    6389640461,
    2930649824,
    5213378636,
    5539656375,
    1892728071,
    1904696112,
    2648076881,
    5103936950,
    2321615032,
    5150458430,
    5138597302,
    1872570870,
    6281053522,
    1644489953,
    1641532820,
    2769301163,
    5848028408,
    2638443953,
    1791039083,
    6519101032,
    6451572457,
    1992609200,
    2973568460,
    1798160113,
    7320555280,
    3120845115,
    2735617350,
    2477538737,
    2960763941,
    1084374933,
    1274460913,
    5892537259,
    2978676377,
    3172988254,
    3760691122,
    2005489873,
    6456774771,
    2135771742,
    3207370702,
    2469382780,
    5921241463,
    6248471088,
    2102638983,
    5687693095,
    1913382117,
    6561869527,
    6597694827,
    1578336500,
    5536208105,
    1941239935,
    1360383920,
    1997404651,
    3469830734,
    2701766190,
    2717507461,
    2231797232,
    3970820202,
    2056346650,
    5314542714,
    2137385272,
    5029973649,
    3509156810,
    5634238919,
    3844617568,
    1926723314,
    3144192467,
    2638304061,
    1891053514,
    3238758592,
    1617416704,
    1642512402,
    2919811837,
    2768168325,
    2503956924,
    6510557968,
    3165101432,
    5492453247,
    6260176874,
    2147552853,
    3199484595,
    1884334303,
    3874268626,
    6355789904,
    3290332213,
    2469063713,
    2288064900,
    2868676035,
    3261391240,
    3746699887,
    1767829987,
    3944553920,
    6229246743,
    5536142809,
    6304111274,
    3361952722,
    1737698092,
    3294364345,
    1928580155,
    6637647680,
    1672519561,
    6595822197,
    5320051585,
    5876565829,
    5271724684,
    2998045524,
    1504847123,
    2824120872,
    3465379640,
    1617416704,
    1642512402,
    2135723402,
    1615799143,
    1604790221,
    1998988241,
    5155859193,
    5661566460,
    5506906732,
    1778234233,
    2625132925,
    1983224183,
    5984477637,
    3163303370,
    5241454796,
    2072023357,
    2133673623,
    1147730247,
    6483824200,
    1917050314,
    3236093652,
    2454236790,
    1172934465,
    1697831582,
    3960905543,
    1729014640,
    1772048580,
    6444140599,
]

count = 0
for uid in uids:
    crawl_person_infos(uid)
    count += 1
    crawler.info("count:" + str(count))
    time.sleep(1)