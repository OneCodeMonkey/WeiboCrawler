import sys
import os
o_path = os.getcwd() # 返回当前工作目录
sys.path.append(o_path) # 添加自己指定的搜索路径

from page_get.user import get_fans_or_followers_ids
from tasks.user import crawl_person_infos
from logger import crawler


uids = [2586541294,1758151867,1611341941,2415183213,2481758501,1835543854,2748257123,3227287623,2003221831,3142459183,1729605197,2412141537,1773743804,2400443637,2496860872,2872046064,1786679143,2477542711,3777289922,1835231167,2537215193,1253984671,5249950879,2134163547,2718959253,1882446913,2419893803,1889684761,2607263643,2403883677,2160031073,2581887155,1917378517,1758467667,1759034967,2729963071,3194089624,2722568243,2506987907,1728119335,1881072435,2352641937,5107824583,2167558983,1947106001,3215771322,2393090561,2733863845,3602419174,2390364953,2440123027,1943044983,2436324877,1903983811,2826377015,1874323965,2911237212,2188358133,2077796707,2341510395,1341774210,2503805521,2198922685,2840157740,2882594004,1921494107,1803814541,3087474293,2953793217,2710128412,1795581917,2126439990,1797770582,2684830057,2378573105,6157747031,2291948210,1979761953,2070059951,2691652217,2387130010,2748593575,2763421155,2922092237,5510578820,1931073924,1772445045,2545020753,3169861162,2063524811,2749424783,1017482731,2820467475,2348613655,1965556147,2822947435,1842368905,5072351954,5181348117,2446569501,2834733977,1752719184,2391864693,1977645535,5445928185,1775884287,2240194587,2909393013,1845678487,2850611023,2161108263,1851932824,2165915774,2658485030,1919675875,5331939744,1949936013,3958190206,2486565747,2467389004,1907704567,2337237827,2111428190,1914418513,2038111197,1828588940,1896380373,2421247151,2648543203,5329686008,1965560255,1780564544,1882402620,1749295257,1974883353,5235083001,2292473137,1987160985,2681049530,1901634771,2475140827,2169202511,1789853693,2034037383,2319287864,2606616007,2513537114,3834871682,2510559737,2791800161,3278260334,1744112151,3215060797,1651042353,2538185830,2653124844,2572820481,1797977753,2370177172,1942265355,1837187452,2813924502,3673379954,1822960757,5209364723,2348393683,5976916217,2352406637,2232484903,3449951754,2186778150,2620385983,1758240267,2353405852,2720730575,1949943267,2881076470,1780313304,1644293537,1892995263,2814765904,2296006221,2001079004,2183238640,2218297431,2054384661,2808756183,2649381443,2338622733,1964365422,1914630415,2487220117,2074755571,2608089683,2791469923,2012466560,2351031193,3570556851,2472480273,1820164051,2130693803,2097018397,2207876914,2030640757,5940184923,1772997840,2717343267,2212288280,6404056670,2634958621,1923691833,2560600931,2734741562,2536800741,2385963127,2529684972,1891915203,2729566867,3189918572,2599751743,2008613075,2390310897,2514836940,2762396365,1778586357,3579835135,1991034807,3098189192,2187731295,3152162782,2465103071,5083063051,1881820545,2607696865,]

# 爬取关注列表
count = 0
for uid in uids:
    result = get_fans_or_followers_ids(uid,2,1)
    for user_id in result:
        crawl_person_infos(user_id)
    count += 1
    crawler.info("count:" + str(count))
