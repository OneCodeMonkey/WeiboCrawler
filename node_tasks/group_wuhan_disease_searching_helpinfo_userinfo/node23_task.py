import sys
import os
import time
o_path = os.getcwd() # 返回当前工作目录
sys.path.append(o_path) # 添加自己指定的搜索路径

from logger import crawler
from tasks.user import crawl_person_infos
from tasks.workers import app

uids = [
    5105486481,
    2114709872,
    1497087080,
    1780524194,
    1249819153,
    2817997422,
    1750070171,
    1810447725,
    2901604625,
    1914665884,
    1910695630,
    2524244845,
    1991619175,
    3625692500,
    1656831930,
    5763590378,
    1728555142,
    6341594574,
    1644459891,
    1549286430,
    5263061859,
    6098024841,
    1877136025,
    1914940461,
    5183167379,
    2853016445,
    1906570245,
    1832245325,
    1686546714,
    2152464567,
    5681417997,
    3213170814,
    2056673925,
    1774057271,
    5120350879,
    6418480627,
    1877471117,
    1946866743,
    5781257600,
    3635909215,
    1642088277,
    6587005000,
    3815441527,
    2411362032,
    3544911160,
    2811365687,
    1008249555,
    1314608344,
    2616332163,
    1926786203,
    3895952436,
    5746643957,
    2862509234,
    5228179675,
    1642512402,
    1903581394,
    3219513881,
    3149831401,
    1911757644,
    2469836092,
    6795992076,
    6510628999,
    3732183044,
    6421121141,
    5591439758,
    3824115966,
    6788499283,
    2498142723,
    1756835451,
    1710226151,
    1651428902,
    3329420380,
    5990753721,
    1767960562,
    7003504621,
    2032375287,
    2926725510,
    3042513584,
    2625132992,
    2658218251,
    5103892319,
    1651428902,
    5284750328,
    7372313440,
    2183542485,
    1743248015,
    6543308790,
    1703769015,
    1479744737,
    3396921562,
    2109885920,
    5639343355,
    2566813090,
    2512533230,
    2546262331,
    2718782231,
    2146046915,
    2994098810,
    6364116325,
    6691926346,
    2712391611,
    1571743761,
    1300425997,
    5801745449,
    1149838491,
    2481602110,
    1762152361,
    3347480634,
    5666170993,
    7203801362,
    5094103156,
    3989157113,
    2469836092,
    6170362439,
    3994415067,
    1934138725,
    2116182794,
    1196952590,
    2697286743,
    3585972593,
    5128351263,
    5033323158,
    3904762344,
    3867177078,
    5529102623,
    5890672121,
    2312075675,
    6107942519,
    2639357221,
    1741801024,
    1940079587,
    3183471901,
    3771857862,
    5172668637,
    2838345860,
    2403982005,
    2685005731,
    3826224034,
    1970239225,
    5591977545,
    5136739800,
    3948683157,
    3229851052,
    3164153407,
    5041348436,
    5832180968,
    1849376214,
    1634365454,
    2456148273,
    1248272901,
    5822209902,
    2853016445,
]

count = 0
for uid in uids:
    crawl_person_infos(uid)
    count += 1
    crawler.info("count:" + str(count))
    time.sleep(1)