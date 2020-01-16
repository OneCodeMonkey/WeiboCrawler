import sys
import os
o_path = os.getcwd() # 返回当前工作目录
sys.path.append(o_path) # 添加自己指定的搜索路径

from page_get.user import get_fans_or_followers_ids
from tasks.user import crawl_person_infos
from logger import crawler


uids = [2274434172,2558003423,3197925284,5234261866,5116301890,2065123907,2244632344,3224206954,2695308095,2884084872,5087967389,2464145267,1740160680,2785836144,2346692943,2249351784,3041170883,2476130202,2008192427,3605666147,2253238873,2189711020,3193922900,2502396885,2635078517,1777632577,2598188774,1978168753,1786332120,3278528104,1809633224,1988950515,3912369460,2397461061,2371061461,3736514400,1844842472,2671079183,1764136300,1791940751,2560139464,2436150320,1923248794,5326359820,2755331353,2339465687,2340106045,2081523495,1656225573,2370284865,1839551994,2764684391,2513391060,5457032441,2546729094,2954112432,2504803547,3477594210,3514361940,1751109332,2724857577,2242693287,2368102452,2733896313,2421628100,2293046734,2427908284,2582483462,2417806572,2563101752,2255108894,2012187290,5065130993,2287392423,2802916972,2596478967,2938152761,2667136130,2748726035,2185841830,1923250723,2710658605,2361870230,3595554831,3120725074,2325322624,3104761881,1793303142,2582817980,2286977544,1793249042,2449385202,2300267675,1796511711,2319942894,2266231590,2431778900,3625431913,2942623821,1810567774,2710410694,2416250592,2127667244,2803887062,2685418194,2379972074,1978408210,2064584805,2356644914,1824499802,3916767634,1875631553,1159852291,2667084761,2265434700,2972908203,2824058657,1781110061,2965517590,2822376824,3950230896,2959836845,1843847345,3848898845,1812947417,1882237414,5100713753,2233153144,2946003407,1976745453,2410611753,1914566603,2142529925,1996429791,1772827284,3177491735,5516638451,2393574950,2006582431,2398964683,3135631323,1981333383,2805906432,3180857030,2248556550,2675307961,1774716915,1972964174,5742970217,1955264753,2567155931,3901021701,2850498192,2487404841,2377356253,2921244700,1777110555,2428068367,5078532598,2679741653,5106130345,2841299004,1979503407,2939264277,2708948051,2509617733,2936368007,2291427397,2115748453,2529284325,1796051677,2695703800,3180486335,2624987883,3152438425,2183250755,2327358860,3656949353,2709447431,1959041951,2307019380,1950728455,1826051984,1876372025,1797755212,2160447750,2073797365,2456025732,1898452451,1949374131,2340617984,2316355251,2255831670,2715736001,2755158947,1743223537,5067333964,2571408750,3608171811,2531345201,1440441075,1653030954,2058969832,1931844103,1440671472,1891679337,2467582372,2476072287,1955531934,1595575394,2629109833,2198266224,2506473297,1440468453,3148389022,1440414790,5681178478,1874068403,5243591767,2035464605,2201274755,1722289741,2299844711,2419870575,1927541867,1977151811,2406823150,2109454613,2031832273,1964469287,2250134885,1875400085,2165331775,1936906025,]

# 爬取关注列表
count = 0
for uid in uids:
    result = get_fans_or_followers_ids(uid,2,1)
    for user_id in result:
        crawl_person_infos(user_id)
    count += 1
    crawler.info("count:" + str(count))
