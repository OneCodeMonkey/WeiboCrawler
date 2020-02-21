import sys
import os
import time
o_path = os.getcwd() # 返回当前工作目录
sys.path.append(o_path) # 添加自己指定的搜索路径

from logger import crawler
from tasks.user import crawl_person_infos
from tasks.workers import app

uids = [
    3617147030,
    1759607415,
    1930424715,
    3556125221,
    5763069683,
    3223766764,
    1718259005,
    1813026943,
    2208511471,
    6003634636,
    2434416140,
    6414541819,
    3314503443,
    5044281310,
    7363954935,
    5533813685,
    6626543590,
    5656459253,
    1769138302,
    1937187173,
    6089703369,
    6416448682,
    1845864154,
    5098950029,
    5096830153,
    1372504382,
    2881698800,
    2697576495,
    2660940103,
    1609566563,
    1592705513,
    6075607310,
    5318906550,
    3989622954,
    2790685082,
    1911757644,
    1497169252,
    1872173755,
    2034145177,
    2977570507,
    6005883208,
    6915896638,
    1777508897,
    3889553744,
    2288691440,
    3242106904,
    2982328151,
    3121654361,
    5791948183,
    1649173367,
    2157730525,
    6223367841,
    3870787200,
    6561147703,
    1617416704,
    6078276017,
    2633589682,
    6213101502,
    5726010915,
    1707612123,
    2342485000,
    2092810043,
    5040955225,
    1991619175,
    5712907053,
    6056011462,
    2607972104,
    1664462585,
    7308673690,
    3037284894,
    7074204911,
    5508619558,
    1301904252,
    1890144872,
    2701766190,
    1829690152,
    1735300360,
    2678317162,
    2271051770,
    1417977805,
    2995411251,
    6066365312,
    1899621707,
    2253302284,
    1806503894,
    2016776675,
    2266137860,
    1841318325,
    1844967414,
    5182171545,
    1895394815,
    5579261611,
    5656415375,
    5872836496,
    5865624216,
    3603732332,
    3546332963,
    5138227215,
    2286386250,
    1884334303,
    1916780343,
    1772824984,
    2259661342,
    1847932683,
    1700315953,
    1650633992,
    1792326131,
    1075970297,
    2656274875,
    1105244233,
    2733235265,
    1644260402,
    2882537514,
    5855783939,
    5296024547,
    6332013811,
    1660069507,
    1615670221,
    6004281123,
    1403611582,
    1960866254,
    1355028413,
    3669267883,
    3495612870,
    2165606235,
    2490707052,
    5816161945,
    6385150810,
    1408036464,
    3053084910,
    5575055843,
    2620088113,
    5019868478,
    5366000231,
    2258727970,
    1770545650,
    1229253383,
    2748747930,
    1859409223,
    2557375422,
    2131593523,
    2010205983,
    1848287180,
    6524697382,
    5734353406,
    3977652730,
    1710390641,
    2321615032,
    2619101432,
    1677991972,
    5928472070,
    2056015491,
    2117522902,
    2645858577,
    3955261359,
]

count = 0
for uid in uids:
    crawl_person_infos(uid)
    count += 1
    crawler.info("count:" + str(count))
    time.sleep(1)