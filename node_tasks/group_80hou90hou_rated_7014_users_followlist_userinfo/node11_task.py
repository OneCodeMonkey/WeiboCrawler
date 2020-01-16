import sys
import os
o_path = os.getcwd() # 返回当前工作目录
sys.path.append(o_path) # 添加自己指定的搜索路径

from page_get.user import get_fans_or_followers_ids
from tasks.user import crawl_person_infos
from logger import crawler


uids = [1785400235,2669638747,1929171601,2383638307,2001609637,5070181549,2123353357,1977022981,2297915373,1753174031,1948544665,2741890432,2037650961,2795542174,3883536742,3240503983,2310705137,3048030594,1795075527,1834620512,1783772002,1793670227,2480876114,3555462065,2104112031,1813308605,2128154093,1758194843,2435840462,1911345153,3657025230,2480384311,2262125311,2580798782,2207534993,3607687977,1843029861,5212637187,2934114377,1927353541,1803723123,2119160773,2117113373,2037824641,1791305373,2429128364,2890462850,2412991007,2318959933,2651442294,2684508011,2804573401,1926464231,2760040161,1832356004,2069055091,2164933935,5025336882,2308821263,2145032391,1813215470,2473558560,1757431755,2988915051,1907169997,5545661331,2340092331,2344227043,2014613675,2805496057,1789300684,2290616241,3209250405,2590117865,1789352581,2750559821,1730629635,2162321661,1786031455,1879603474,2107389081,2526514235,2756409360,3034755427,2285916037,2257827980,1810459745,2027838687,1781578145,1782418465,1973179173,2583263304,1773004354,2309296423,1768252955,2179632032,2357913323,2504397663,2338056127,2606646611,3093509703,2113353663,2849835667,2828327752,1862695663,2407486225,2574338400,2119990715,2398070317,2355277974,3226731701,2571284760,2687539232,2760549773,2014182352,2285813443,3031977314,2681692031,1802724844,2560058960,1784069410,2504117312,5311121264,2062786240,2535819121,1883581411,3225038743,1881081484,2662275861,2518279430,2698550841,1233923157,1971268235,2397909021,1816426260,3027768465,1938045717,1580452920,2434313584,1772473724,2316065195,2910736681,1833205235,2628669890,2453503591,2607275281,2327352551,2297163593,5683673540,2701476800,1807395487,2018549561,2189486295,2729466520,1923100490,1824800902,2289497765,3136507167,2369793370,2772730594,2442740995,2233819407,2245737891,2200904787,1822696662,1784153453,2383169643,1318318084,2035014660,2795113834,2651609004,2412841925,2660484937,5646560435,2466884717,5139121662,3517522227,2852668470,3177948787,3740298150,2402673981,2385101242,2590250661,2139436432,2974765850,1804330061,2305379865,2214591293,2983893463,1830213785,2235117627,2297969075,2272814230,1799249803,2558405243,2514119104,3748347084,2654840984,2132371563,1768965635,2420431824,1823915712,2318401363,3212009943,3861945927,2706569485,2278067061,2339627241,1821030173,2801052422,2771099695,2433405591,3228074742,2572332242,1836406510,3946456220,2142959980,2239576600,1870205382,2716136063,2637697370,1875243442,3196640231,1764883260,2442209770,3127154135,2039953037,1773718984,2576518242,3193149637,2607630635,2270510865,3952188774,1789234257,]

# 爬取关注列表
count = 0
for uid in uids:
    result = get_fans_or_followers_ids(uid,2,1)
    for user_id in result:
        crawl_person_infos(user_id)
    count += 1
    crawler.info("count:" + str(count))
