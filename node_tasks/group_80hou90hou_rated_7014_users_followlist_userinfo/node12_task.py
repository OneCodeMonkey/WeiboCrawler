import sys
import os
o_path = os.getcwd() # 返回当前工作目录
sys.path.append(o_path) # 添加自己指定的搜索路径

from page_get.user import get_fans_or_followers_ids
from tasks.user import crawl_person_infos
from logger import crawler


uids = [2288657833,2524839532,3974662645,1983196215,3479691887,1816789123,2958742634,2781215384,5048107322,2214113043,2645046010,1977110383,2127987103,2538628101,2437746452,2261456470,3277953095,2294020922,1875397360,2096800033,2362567590,2193876590,1940500637,2649970757,2305025504,2450660332,1748332917,2453810905,1874001712,2178578782,2629451481,2273474500,2628524973,3216658745,1843619783,2360482654,1960680363,2400837670,2045451730,1601718764,2836464504,2980869711,2705663962,2471139242,1810465827,2672239874,1644750057,1865115244,1879176013,1958047141,2832388751,1758658743,1785208501,1909482081,2035497237,2048376913,1671822017,2002555503,2346565272,2544996985,1885992044,1793080985,2423093400,5163527946,2202680382,2405392124,2323419841,2276327785,1991721365,2706482202,1862257782,2439838012,3029681915,2609788752,2700353510,2399127153,2707487225,2566924183,2371661741,2306424713,2175748012,2885311052,2835822522,1829877750,2570229031,2181966780,2405689577,3220761921,2806367362,5318332006,1793704585,2406737637,2297970160,2123787150,1840566944,1867827124,3841337936,3334688244,2388303981,2720837831,2431759214,2215017362,2862625974,2170231824,1917557342,2298214144,1630787485,1935012444,3119190933,3537101962,2275938830,2311900994,2358798913,5208688822,2286678235,1853010523,2693731980,5065737993,2577143740,2580158842,1706125350,2258724184,2390773154,1769862934,2705489673,2185821800,1774862330,1816723222,2384366142,1935900415,2625522915,1274902920,2859223172,2245232755,2178148051,2496606491,1863971414,5283579802,2709713665,2302831040,1806584154,1840227975,3464133844,2974030014,2881265020,1772411064,3460131164,2709354883,2156416287,2750290531,2390013594,2589748807,2219515820,2433559972,2442049884,1787562050,2387816215,2092712671,2689843497,1853490251,2065331115,2934586693,2184067564,3180822407,2433973947,1922079883,2300435963,2570130285,2044348347,1980326620,2314292180,2957020380,2644117682,1609465095,2681233000,5128553664,2637983521,3194630227,2169350404,2496233742,3100158583,2496390112,2728805507,2711615275,2392669487,2401710262,2662956903,2580844564,2433841787,1794743760,2178014882,2556385630,2397179192,1771771340,3431064830,1760715791,2841636991,2846946230,2445347087,1822249347,2952424473,1624719953,3383103980,2453119161,3919085984,2411541551,2751785055,2292834297,2656685641,2708301751,2424190831,2052597381,2647342625,2099196401,2356722583,2473719640,2875635784,2295243212,1906316923,1772988811,1909103725,3730879762,2375467184,2211591301,2752557457,2103303512,2384714580,2367885304,2870567094,3308401823,2173772697,3158151170,3161243634,1944119491,]

# 爬取关注列表
count = 0
for uid in uids:
    result = get_fans_or_followers_ids(uid,2,1)
    for user_id in result:
        crawl_person_infos(user_id)
    count += 1
    crawler.info("count:" + str(count))
