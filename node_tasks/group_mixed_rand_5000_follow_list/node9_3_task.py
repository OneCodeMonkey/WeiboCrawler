from tasks.workers import app
from page_get.user import get_fans_or_followers_ids
from tasks.user import crawl_person_infos


uids = [2643484593,5586062169,5889818377,3164953615,1971071013,6458075269,1817394440,3260000225,2095485407,1361741047,1073896671,1969520911,1846113022,1663668520,3813080309,2319127227,3951144899,1719737017,2058557890,5044882617,1775984957,2104673894,5068166438,1167181262,1899986697,5813614801,1752091114,2858793390,3948645369,2404823483,1866889907,5073293374,2260624322,3517227832,2844501801,2120210322,1588153507,1420197772,5246748269,1110292527,5356603018,2136968802,2041548447,1884901650,2203790764,1820644037,1923216587,3110440575,1941092965,3220557132,6196530691,1396831532,1775777125,1891258241,1572602121,5353457606,2061135073,1761977804,5043100329,2281985792,1668782455,3822594109,1990919581,6432711826,5213215629,1355147361,2821251572,2519426890,3966816329,2771245205,1211911162,5970370690,2181246654,1563021065,1886012702,2814395305,2101489932,1760484052,2422476194,2438017923,1883052805,1887880322,5936732412,1690125563,2493096224,1910064391,7029341518,2143047911,6600797452,1686464862,1651964181,1873347354,2682045371,1750384103,2021784017,1919955961,1895283041,2150445042,2090733153,1651208437,2038052170,2038941630,2686715671,3516816434,1418333531,2970341801,2613552497,1804024325,5200741840,2007950801,2240354055,2105553811,2615579602,1798865184,1730347055,1835513903,1652605345,1633951802,3066968127,3175508733,1833374792,1895223594,3953697868,1848912660,2721457735,3035421633,1860668927,2107707510,5834772989,1736468617,2284289437,1869670695,1779736985,2101384622,2760150154,3089013230,1768184703,1794421801,1991881781,2688438032,2514050771,2082479713,2198793392,1729280930,2852113641,2016814761,2419740013,2966596692,1736136293,3163833177,5044317035,1172951673,1743402035,1773224075,1739536704,3167293425,1819492193,1258164695,2111968443,2305036672,5570968551,1696654744,2628304433,2101352434,2424725940,1818022540,2373598892,]

# 爬取关注列表
for uid in uids:
    result = get_fans_or_followers_ids(uid,2,1)
    for user_id in result:
        crawl_person_infos(user_id)