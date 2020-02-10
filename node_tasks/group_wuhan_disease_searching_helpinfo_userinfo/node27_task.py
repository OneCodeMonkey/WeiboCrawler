import sys
import os
import time
o_path = os.getcwd() # 返回当前工作目录
sys.path.append(o_path) # 添加自己指定的搜索路径

from logger import crawler
from tasks.user import crawl_person_infos
from tasks.workers import app

uids = [
    1916526055,
    3647450142,
    5676360941,
    2048669145,
    1767910704,
    5932962040,
    1750349240,
    2409479697,
    5215729787,
    5767479764,
    1650306147,
    2077905117,
    5155207590,
    2785906430,
    5683204700,
    1960660265,
    6860053083,
    1105244233,
    2637942951,
    2418201593,
    5897816720,
    3217001275,
    2309793941,
    2179601487,
    3041416501,
    1837869620,
    2881520352,
    2049389352,
    2208160981,
    3962766317,
    6278572236,
    2637942951,
    1988645095,
    6926438705,
    1633435427,
    5861857092,
    7282830801,
    2936780754,
    68254022,
    6171488993,
    2649470421,
    2824120872,
    6444741998,
    1644459891,
    2239602283,
    6636571890,
    5714943066,
    5098525683,
    6873924036,
    5887882449,
    3060590437,
    2081296667,
    3192049235,
    1847582585,
    5113485362,
    5749471015,
    1651171992,
    2178865082,
    1675961211,
    2469562734,
    2526210970,
    2346031615,
    6337398027,
    5065787799,
    5332840563,
    2359224985,
    1833864964,
    1769165581,
    5035436797,
    2038340521,
    3728240585,
    5558990115,
    1826111997,
    6244639794,
    3939426052,
    5492453247,
    2266187623,
    2280198017,
    5870153930,
    5506906732,
    1961594843,
    3486040040,
    5519375550,
    6299759649,
    2534060201,
    3762081067,
    2171757642,
    3788559921,
    3077235957,
    1953841077,
    5623853674,
    3635266085,
    1960660265,
    6262687783,
    5661566460,
    6476967019,
    5461921176,
    2998045524,
    1784473157,
    3144706550,
    2178979330,
    2747973904,
    5655420911,
    1652484947,
    6152261837,
    2720808113,
    2881099692,
    5558990115,
    5698641249,
    2157730525,
    6109428342,
    5213379204,
    2883941882,
    6003634636,
    1959444680,
    5285409500,
    5692872461,
    2343651831,
    3002094814,
    6136547022,
    2613472455,
    2469836092,
    2167406082,
    3950759014,
    2230861607,
    6448078885,
    2482121251,
    1506142182,
    1735300360,
    6577966050,
    1738175595,
    2470544165,
    1159186937,
    5332840563,
    1614248297,
    2875485731,
    6866290423,
    5127676903,
    3257048965,
    1066582722,
    2214887995,
    6027731978,
    1826594470,
    3036656427,
    2075245652,
    3171944275,
    1915671961,
    2049389352,
    3911617807,
    5269917567,
    2744925381,
    6395447431,
]

count = 0
for uid in uids:
    crawl_person_infos(uid)
    count += 1
    crawler.info("count:" + str(count))
    time.sleep(1)