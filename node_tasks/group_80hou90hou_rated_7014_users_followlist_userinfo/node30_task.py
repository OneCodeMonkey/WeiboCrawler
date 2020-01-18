import sys
import os
o_path = os.getcwd() # 返回当前工作目录
sys.path.append(o_path) # 添加自己指定的搜索路径

from page_get.user import get_fans_or_followers_ids
from tasks.user import crawl_person_infos
from logger import crawler


uids = [2104317783,1904601335,1857210832,1890595291,2324024635,6283321815,2466804970,1796665821,1847306783,1862698680,1194750851,1746383041,1294181721,2045960750,1863927724,2516814315,1733241811,2021801707,2474788080,1962498275,2429221237,5173727030,2098224262,1869794061,2237228004,1740088300,1492508417,2695781952,2457606200,1745629597,1781159082,2677293113,1784872007,2627592701,1764895497,2159279123,1919897460,1691092253,1926470313,2125682913,1133367772,2185016774,2097819254,1959150190,1663110042,2798569754,1837899523,2989851882,2009052945,1741116511,2149037384,2720945535,1748789580,1785896850,2304991685,1758240147,1324613944,5209657271,1942881755,2253756847,2315331097,2490103207,1862492497,2479980091,1953197897,2460358393,1791269164,2411801215,2174997072,2083026771,2735602941,1762596085,2629467163,1983733123,2607437881,2118922287,2092497115,1869899075,1765569542,2112822893,2598582662,1777397594,2127977745,2312920817,2714627500,1735403511,5319312980,1741871474,1954300121,2004541591,2546366450,1877328472,2096968782,1834326570,2218960174,2409257954,2004332361,2232076463,1865422570,2683179505,1588292623,1901051185,2019354435,1748384527,2724673041,1729465501,1731840440,1768409950,1864030464,5287838857,1788870765,2144350375,1881255880,1282401261,2023412562,1424848041,1791162681,1742188754,1563401082,1358794233,2050724340,1779895190,2070645160,1772278353,2101802157,1904778207,1519924380,1978371031,2071615021,2394794335,2472300850,2629327843,1624896360,2099642672,1837160105,1739116767,1573059015,2159081001,1884218430,1998104091,1340395787,1678099075,1928121627,2213136200,1905567082,1570355930,2157966115,1993501560,2185032675,1857052190,1539145741,1735683030,1807866284,2793620222,2428278761,1766840980,2102205634,2295993410,1854342345,1732415715,1938567322,2214839842,1767485244,2269153794,2553171361,1747096601,1773191250,1778157035,2253245347,2063130477,1428784347,1883708342,1929965201,2465978984,1757306631,3082588947,2500862722,2186210467,1641511401,1744313517,2015078281,1767652314,2388266020,2047704311,2567796994,1798592003,1864622455,1651498372,1717083954,1699919670,1842894705,1978779231,1093185102,2976075015,2073339984,2238159584,1989520301,1807030597,1594257344,1449069683,2346597240,1778307265,2368670477,1302019601,2128978341,2267990392,2343744114,1723723903,1628933762,2101555341,1778131910,1840401982,1776579112,1828631672,1724720903,5951224843,1977652061,1803366787,1777880534,1773457387,1778381464,1727550717,1778242044,2708715673,1921251283,1268580931,1828266423,2293252911,]

# 爬取关注列表
count = 0
for uid in uids:
    result = get_fans_or_followers_ids(uid,2,1)
    for user_id in result:
        crawl_person_infos(user_id)
    count += 1
    crawler.info("count:" + str(count))