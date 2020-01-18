import sys
import os
o_path = os.getcwd() # 返回当前工作目录
sys.path.append(o_path) # 添加自己指定的搜索路径

from page_get.user import get_fans_or_followers_ids
from tasks.user import crawl_person_infos
from logger import crawler


uids = [1907244065,1805372073,2388154434,1751486907,2214962382,2501205174,2694377973,1864650557,1795318910,2295134257,1864058712,2706052552,1762157624,2683278130,2792616851,2459078470,2281373802,2157330894,2394181221,2043558975,1851975261,2476254740,1790026110,2187619680,2647286152,2589020891,2342390874,1984938023,3226219693,1747255760,1728230517,2030589023,2786470214,2909435031,2527681505,2923579617,2119126035,1949739980,1809588114,2164780854,1851943537,3043821342,2315561803,2886323352,1847392364,1611795934,2521945994,2406281270,2649968670,2586125454,5401528078,2167170442,2548243342,2674182761,2172430223,2091068671,2436901390,1806467677,2088190667,2023547473,2901363313,3516445307,2301100971,2756612703,2149258063,2854237832,2447864174,2424970550,2984083712,1991464081,2293462700,2161211910,1902117571,2451945373,2284577391,2686890451,2345574002,1937183301,1750886277,2669732770,1886317257,2142411845,2668799675,2613218075,1967145981,1883860474,2632861054,3028326933,2314796842,2585636274,2169021327,1774583083,2951834224,2191909064,2012790482,2445266471,1906402561,2297290020,2690950421,1860880770,2269972012,1647042090,2456830692,5616935814,5089436666,2556714493,1649797972,2583843600,2434583645,1784462311,2312466833,5632889180,3123556371,1941311715,2133079061,1751115101,2217522810,2031968767,2073197907,1876130957,1876499705,2122788635,2217220984,3221257422,1782738471,2122584580,3913737904,1940004751,2101718811,2783199094,2311587647,2144217683,2315997045,2446185724,2473301717,2127994480,2319633087,2397991427,2885910933,2139933734,2624084017,2120461220,2522122857,1779758085,5625790463,2939513447,1924118841,2231466394,2288083425,2437251270,2288710930,1758332591,2783090250,1736636385,2455156641,2571419584,1861432367,1737386830,2369566422,5610141905,1818804194,1904175580,1798728064,2255961730,2842353972,2164335882,2210992540,2421963882,1775851191,5312010668,2447463987,2966061692,1746786742,2048541765,2819332004,2176717455,2344740630,2267871251,2693073031,1967146113,2009356672,1727244085,2163926505,1778435422,2037502303,2319773181,1961806393,2295540320,2469382913,2631248834,3037154107,1850926124,1740801864,2124131513,2344268117,2541722111,2443798862,2198938680,2434232153,2122868445,2601796205,5508224600,3178300512,3453412250,2647748655,1744952985,1806328590,1826487890,2283172292,2060952523,1686995031,1804875014,1843170525,1750463145,1762560170,2698520484,1879598392,2692741810,1911323222,2182766343,2135707487,2443312477,1797231852,1951333181,1773360404,2500839977,1662871743,2582466597,2160934432,2373573903,2517755301,1721136417,2649653972,2164955034,]

# 爬取关注列表
count = 0
for uid in uids:
    result = get_fans_or_followers_ids(uid,2,1)
    for user_id in result:
        crawl_person_infos(user_id)
    count += 1
    crawler.info("count:" + str(count))