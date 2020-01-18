import sys
import os
o_path = os.getcwd() # 返回当前工作目录
sys.path.append(o_path) # 添加自己指定的搜索路径

from page_get.user import get_fans_or_followers_ids
from tasks.user import crawl_person_infos
from logger import crawler


# uids = [2257700715,2324062003,2350190277,1964220353,2872536132,3221262175,2054774633,2046850341,2453317911,2169956391,2429818685,3180555740,1831765897,3686912192,2515609974,3466163512,2476919587,1867477204,2184324314,2665601753,3597377344,3231181290,1855173673,2136173411,3419074442,2244334917,2205819227,2325153473,1728129674,2434923241,2490466357,2307617754,3122370204,2404585853,2218353933,3264906811,2832512205,2684254843,2112122331,3177914774,1910191887,1762959273,5093037203,5187706971,5894235981,1686147704,1793608821,3148211550,2822776980,5436860164,2717578543,5116168950,2215462587,1949534113,3218132693,1918461763,1993657483,2995238515,5664017681,2733736867,1995768317,2670681531,1901236102,2381523485,2516009924,2008460815,1909934485,1735464051,1791290455,1849502323,1799415561,2761560201,2384224094,2639457360,2230191245,2574288451,1834047673,2174190631,2300568675,3238673234,1823077225,3228749493,5238454627,2824148807,3867842039,2713835602,2604912657,1835509102,2293816223,1761128301,2399643224,1866697833,2733736403,3017704801,5493453507,2473501381,2718844823,5210606539,3284013325,2651734492,2883983597,1842180607,5323984025,5371852561,2006996427,2479065190,1757763915,2232833815,2729178851,1904889392,2731368371,1786005983,5224345947,3228462267,3076439981,2650584663,2251326835,2161143151,1663489117,2083267837,5317754459,2834605175,1949545071,1789429511,2728531132,3096546891,5545348057,2030060237,2281588941,1869091331,2277251187,7190394629,3855755864,2656058093,2309086917,5481853682,2703386765,3568555710,1902220343,1967179271,2640377683,1974982943,1915111957,1969160397,2713345862,1752961257,2314236412,2100849973,3993744842,2302495767,2283838394,1844149581,2958374311,2427343054,1945942721,2231420667,1958972661,2419598581,3504041772,2548410713,1934560523,1948302027,1831845477,2334904904,2212134513,2620714685,2039357093,3670055063,2516114472,1915459901,2563286494,2268078687,2655967843,3294304725,2327854501,2835502461,2403242441,2308278713,2550420434,2294657661,3952601572,2933680744,3939940327,5654090159,1594130201,1713909042,2546841935,1963943873,2773351373,2886198675,1974813175,5657222868,1993253730,2296646267,2609300831,3206824630,2609475063,2423875421,1970948467,1842284410,3323027112,2482249212,2208116703,2189208033,1948125732,1877941552,2886343297,2530588680,5595379645,2861656984,2381311017,1792467035,2789794607,2513928705,5653097743,2411850123,1854846435,2842471082,2629557921,1884562675,5088700714,3149604351,2985313053,2974450425,2396704237,1930281467,1969621221,2329688481,3217213510,6132266128,1949625333,2775899417,1911710022,2394050971,]
uids = [3993744842,2302495767,2283838394,1844149581,2958374311,2427343054,1945942721,2231420667,1958972661,2419598581,3504041772,2548410713,1934560523,1948302027,1831845477,2334904904,2212134513,2620714685,2039357093,3670055063,2516114472,1915459901,2563286494,2268078687,2655967843,3294304725,2327854501,2835502461,2403242441,2308278713,2550420434,2294657661,3952601572,2933680744,3939940327,5654090159,1594130201,1713909042,2546841935,1963943873,2773351373,2886198675,1974813175,5657222868,1993253730,2296646267,2609300831,3206824630,2609475063,2423875421,1970948467,1842284410,3323027112,2482249212,2208116703,2189208033,1948125732,1877941552,2886343297,2530588680,5595379645,2861656984,2381311017,1792467035,2789794607,2513928705,5653097743,2411850123,1854846435,2842471082,2629557921,1884562675,5088700714,3149604351,2985313053,2974450425,2396704237,1930281467,1969621221,2329688481,3217213510,6132266128,1949625333,2775899417,1911710022,2394050971,]

# 爬取关注列表
count = 0
for uid in uids:
    result = get_fans_or_followers_ids(uid,2,1)
    for user_id in result:
        crawl_person_infos(user_id)
    count += 1
    crawler.info("count:" + str(count))
