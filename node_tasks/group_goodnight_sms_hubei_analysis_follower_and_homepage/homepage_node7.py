import sys
import os
o_path = os.getcwd() # 返回当前工作目录
sys.path.append(o_path) # 添加自己指定的搜索路径

from tasks.user import crawl_person_infos
from tasks.home import crawl_weibo_datas
import time

# 全部（原创+转发）首页
uids = [5173661702,
1937142950,
1379674067,
1651889760,
3319507115,
2640659690,
5945704462,
5945704462,
5662526846,
3085286621,
2292810891,
3909171325,
1390759412,
2343119383,
1957680867,
1957680867,
1921469503,
3212388047,
5945704462,
2026026725,
1282630683,
2110287535,
1907924542,
3052205493,
3973936240,
5881139451,
2166141104,
2408552654,
1571640404,
2469556584,
2707994072,
1731388594,
1866694863,
1336308067,
3313459692,
1890087084,
1756876135,
1966332294,
5793186218,
5306636732,
3913654311,
3212388047,
2423525050,
1980298501,
1899157527,
6130672858,
1871365404,
1700201371,
6130672858,
2462457237,
3097174037,
2266426014,
2390158900,
3171286800,
1399476561,
1772296884,
5884952637,
6406397026,
1801774532,
2142973391,
3170894117,
5933025113,
6514535570,
2751159624,
1907924542,
5983151647,
5519841669,

]

for uid in uids:
    crawl_person_infos(uid)

    crawl_weibo_datas(uid)
    time.sleep(1)