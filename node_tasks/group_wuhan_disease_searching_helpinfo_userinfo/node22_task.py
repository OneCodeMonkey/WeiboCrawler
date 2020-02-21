import sys
import os
import time
o_path = os.getcwd() # 返回当前工作目录
sys.path.append(o_path) # 添加自己指定的搜索路径

from logger import crawler
from tasks.user import crawl_person_infos
from tasks.workers import app

uids = [
    2606046724,
    2146617547,
    1458160192,
    5181265843,
    2165701080,
    3485977652,
    6026862273,
    5152337091,
    1992998001,
    3509389214,
    1470741277,
    2089358175,
    6632020030,
    1744332207,
    3203137375,
    2271193465,
    1092019621,
    1845488444,
    5926714774,
    1752883611,
    1871765890,
    1589041013,
    1593131864,
    1404360052,
    6003634636,
    2099459175,
    1946866743,
    3649965891,
    1999404300,
    2208511471,
    1847932683,
    1698857957,
    5575268705,
    6313099371,
    1809009220,
    3882593506,
    1686546714,
    1932051565,
    1876871603,
    5051077448,
    1964054151,
    6788499283,
    2304458574,
    1670703151,
    2664422077,
    6514077838,
    3729611330,
    5943595658,
    6525198200,
    2647693153,
    5125089679,
    3848311310,
    2959453074,
    3200353973,
    5621329677,
    6788499283,
    6089703369,
    5177167708,
    6066365312,
    6085714818,
    5491816666,
    1865304640,
    1094627834,
    1909377960,
    2391135893,
    5645914761,
    2568309141,
    5827372660,
    2162541102,
    1882384753,
    1683445890,
    2431035101,
    1642088277,
    1642512402,
    5536367977,
    1821797847,
    1728948692,
    5674314180,
    3839210097,
    5146665915,
    6502569261,
    1420157965,
    2635824201,
    1909250714,
    5909167185,
    1977608227,
    1641561812,
    1909377960,
    2183570524,
    2451789741,
    2862774965,
    1807715644,
    2184728493,
    1897416061,
    1926811743,
    3519636402,
    1236368534,
    5309898644,
    5997389756,
    6541154893,
    2717190051,
    3950902278,
    2267118313,
    3535396574,
    1323527941,
    3797373373,
    1744347587,
    6643264180,
    1750349240,
    2240440333,
    2815224714,
    3764071421,
    2644982532,
    6304111274,
    1528372860,
    3283852551,
    1652484947,
    3240219544,
    1914098063,
    6853056126,
    5298024126,
    6068931036,
    2759348142,
    3149590555,
    6372937418,
    2094318234,
    3744503327,
    1960601312,
    1730243272,
    2973568460,
    5964184998,
    5872828878,
    2760198404,
    5428690360,
    1906592371,
    3798024537,
    2018201374,
    5178570128,
    5548083696,
    3436419330,
    3233576053,
    1717833412,
    3203930743,
    6201552676,
    6323197089,
    1895394815,
    1608454424,
    6217269035,
    1576147232,
    6383246889,
    1704259030,
    6984819294,
]

count = 0
for uid in uids:
    crawl_person_infos(uid)
    count += 1
    crawler.info("count:" + str(count))
    time.sleep(1)