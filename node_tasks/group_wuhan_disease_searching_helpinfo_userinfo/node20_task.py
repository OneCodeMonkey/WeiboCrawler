import sys
import os
import time
o_path = os.getcwd() # 返回当前工作目录
sys.path.append(o_path) # 添加自己指定的搜索路径

from logger import crawler
from tasks.user import crawl_person_infos
from tasks.workers import app

uids = [
    6141969281,
    3363379730,
    6798059533,
    5601415117,
    6421121141,
    2151949447,
    3565722834,
    1728829263,
    1658951274,
    1455543965,
    5099348270,
    3825069436,
    3148001912,
    6021596972,
    1779526875,
    1043320390,
    1960785875,
    1844545275,
    5645893201,
    5478028657,
    2953165853,
    6798080598,
    1850021800,
    5128599868,
    2710077380,
    1974576991,
    5641724922,
    2703487521,
    3920994587,
    2047595554,
    5645756008,
    1806325914,
    1768470921,
    2508689930,
    3980577085,
    5639323283,
    5566625451,
    1821499183,
    5143250102,
    1685770970,
    1918021250,
    1592259280,
    2715361774,
    2661992301,
    5964550870,
    1780511285,
    2827102952,
    1837869620,
    6040549176,
    3204747583,
    5648778366,
    1051119577,
    6131780722,
    1274460913,
    2469836092,
    1397694097,
    5683413309,
    2812067655,
    6606369136,
    5242441982,
    1612622607,
    5038942729,
    5324777856,
    1712102637,
    2039753857,
    5495770083,
    2798817053,
    1598078571,
    1036117702,
    2412053137,
    2348789730,
    1738526387,
    5838001176,
    1409974037,
    1663072851,
    6003634636,
    5336062062,
    1634365454,
    3025049951,
    7100405757,
    1943718134,
    5141350722,
    5290550763,
    2034347300,
    1732294227,
    6415768116,
    1906592371,
    1706480274,
    1410484667,
    2458393191,
    1656737654,
    3754192351,
    1309875855,
    3728240585,
    2827102952,
    6361491468,
    1034227913,
    1821499183,
    5338684015,
    1786583085,
    2028810631,
    1291926192,
    2389641745,
    5513941145,
    5545557263,
    1771281354,
    1142648704,
    1947792782,
    1602718352,
    1624137625,
    2428995052,
    2487490407,
    3975791426,
    2891952684,
    1837701072,
    1789250890,
    5532395995,
    5033190714,
    1879778060,
    3193124930,
    5280254455,
    3178599262,
    2210099714,
    1248924493,
    6572913211,
    6515472165,
    5526399726,
    6163775731,
    1700315953,
    1311446843,
    1740555362,
    6471536698,
    2803301701,
    2539961154,
    2511562732,
    2455136917,
    5674864838,
    2971640487,
    1997412091,
    6088077697,
    1651913544,
    2471070454,
    2436438110,
    2088632431,
    5241454796,
    2087875965,
    3004863425,
    2482981913,
    1884488621,
    2711987451,
    2462258315,
    3840768703,
]

count = 0
for uid in uids:
    crawl_person_infos(uid)
    count += 1
    crawler.info("count:" + str(count))
    time.sleep(1)