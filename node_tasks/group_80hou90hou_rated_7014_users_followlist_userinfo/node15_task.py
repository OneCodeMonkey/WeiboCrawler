import sys
import os
o_path = os.getcwd() # 返回当前工作目录
sys.path.append(o_path) # 添加自己指定的搜索路径

from page_get.user import get_fans_or_followers_ids
from tasks.user import crawl_person_infos
from logger import crawler


uids = [1930213593,1237772774,5434833492,1911655593,2294501681,1908190513,1903169507,3958372170,2305473450,2878137664,1979848583,1970879565,2634593821,3185349162,3142406445,1837876362,1794269645,2949060601,2402170160,2956170144,2679540562,2214809242,2813125822,5486784042,2421786852,1828138907,1743117111,1856062037,2675659544,2863786640,2163486824,5312787256,3196282953,2927581307,2769390097,3091761794,1940630727,2011885057,2063144021,2802740524,1942574355,2512670940,2178503984,1743057331,5206638845,2799630220,2717550353,2687363164,2355284822,2159449602,1870236422,2403588004,3071691863,3149536240,1839100263,2113441613,1789520713,3242777804,2010577727,2301589064,2804750301,2536856673,1976127582,2297607022,1858247751,1763023712,5368181127,2605759122,1891435900,3795117937,5207039829,1876080357,2433605073,2956037484,2465456735,1929735194,2742319745,2849029170,2319767594,2881804952,1776228191,1965074007,2388358804,2678954105,2256008790,2190186500,2196117100,1971383907,1791960990,2503348470,2294245965,3640409684,2232017357,3729889182,2696398791,5643260251,2691917883,2262556854,2256457105,2443421163,1781326170,3991543128,3478128727,2503584222,2104733003,2156895047,2038370205,2155407923,2350065542,2630336801,2843486840,1949696025,1650546142,2448040880,1966734071,1985189191,2319082903,2741065965,6270524058,1929930975,2400662535,2177453460,2368866300,2675765124,2559209302,6070606503,1979458253,1901639135,2608320697,2704228515,2610922735,1941850004,2842409134,2432442064,2811917604,2438921510,2964253872,2009185765,1978760981,3014484197,1810654112,1761657260,2322056144,2091612827,2639588743,2174940061,2726610627,2475838102,5266648436,2676367353,2883734641,2881104014,2901852157,2002799115,1624083991,2744846434,5536634541,2406285945,2234061634,5504666795,2401697135,1605182213,2124934745,1914404177,2624140233,2501301873,2863001474,2301812205,2097495807,1578141194,3339534792,2268704921,1936366643,2704842745,1847314182,1891187751,5676938382,2419265024,2450563487,1994812531,2924088523,2486270763,3911430874,2345300645,1783830703,1804710735,2110733915,1783404635,2841838562,3740859203,1871931142,3899465348,1859488820,1959442264,2186421075,2612124673,2355692921,2535639060,2557930740,2480140560,1808007004,1950879141,2418336807,3258650667,1743930232,2008837237,2006164683,2342073653,2014969187,3090172095,1786876124,2496527264,1767299885,2637440664,1896011712,2128478393,2645084681,2100799947,1796715420,2109141921,2286070182,2389140420,2239219974,2881019660,2365148852,2651997753,1747798925,1880321004,5661618388,1826877264,2122590250,1804566110,2442600871,1919062565,]

# 爬取关注列表
count = 0
for uid in uids:
    result = get_fans_or_followers_ids(uid,2,1)
    for user_id in result:
        crawl_person_infos(user_id)
    count += 1
    crawler.info("count:" + str(count))