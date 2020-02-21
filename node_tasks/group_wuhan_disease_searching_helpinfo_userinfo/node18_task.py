import sys
import os
import time
o_path = os.getcwd() # 返回当前工作目录
sys.path.append(o_path) # 添加自己指定的搜索路径

from logger import crawler
from tasks.user import crawl_person_infos
from tasks.workers import app

uids = [
    1637828795,
    1305431810,
    1736849490,
    6508840982,
    3797815453,
    5576889864,
    3826710669,
    2950461603,
    2541592687,
    5879829259,
    3182698757,
    2694928225,
    3850074943,
    5868119416,
    5484553224,
    1827939580,
    7235324242,
    1219182541,
    6937815716,
    5070502937,
    5035975121,
    2196687115,
    3374171834,
    3936431121,
    1804011592,
    1954461897,
    1717833412,
    2067610195,
    3842046030,
    1911630795,
    6636571890,
    1705494617,
    1824294280,
    6637647680,
    5792003376,
    1933700172,
    1745643595,
    5076875086,
    6329618180,
    5607174069,
    2708325740,
    6524418575,
    1936119834,
    6439240024,
    1966027330,
    2975227570,
    1921898215,
    3204782330,
    3339740470,
    1802564537,
    3834280812,
    6440331204,
    5793220992,
    5742786936,
    1611255281,
    3085996887,
    3822419031,
    6164857032,
    5086253735,
    1719519617,
    1699540307,
    5450295124,
    1418721617,
    1298876313,
    5136561027,
    2087996062,
    1663414103,
    3908071146,
    2183542485,
    1791039083,
    1710439743,
    2218488722,
    1940087542,
    3557414151,
    6849915621,
    5773984868,
    1908194624,
    2643957527,
    1781994914,
    1899621707,
    1769165581,
    2607972104,
    3087714670,
    2139684615,
    6675656775,
    2797392924,
    1947792782,
    2330528562,
    1816852673,
    3979674083,
    5353058678,
    5041153629,
    2607972104,
    5633432155,
    5285409500,
    5647132523,
    3180451553,
    1649195742,
    1886099274,
    3169256801,
    2908013455,
    1233905015,
    1686546714,
    5545578925,
    6072764868,
    1962748933,
    3121311382,
    3818846748,
    2004156837,
    1618051664,
    2430068137,
    3754192351,
    1261823123,
    6207911580,
    5864631680,
    5265246312,
    5846672610,
    1288429914,
    3646648524,
    2967529507,
    5467830856,
    2517950371,
    6115137930,
    2342243655,
    2709036623,
    1906592371,
    1310490382,
    6052678469,
    5044281310,
    1496814565,
    5103376375,
    1503491352,
    3932563582,
    2726417763,
    2046263187,
    2426236165,
    2080045337,
    5867962564,
    1600603027,
    1573472362,
    2214507411,
    2873459380,
    1831649901,
    1862427780,
    6938280009,
    1906592371,
    3240219544,
    5829921460,
    5044281310,
    3546862743,
    6711557653,
    1720038883,
]

count = 0
for uid in uids:
    crawl_person_infos(uid)
    count += 1
    crawler.info("count:" + str(count))
    time.sleep(1)