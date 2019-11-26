from tasks.user import crawl_person_infos
from tasks.home import crawl_weibo_datas
import time

# 混合
uids = [1911488127,3796040541,2646655924,1871566340,2972383810,1925063781,2035877313,1961890761,2478612912,2038139153,2281863214,1595563793,3134392427,2926560393,2319318652,2260624322,2134921051,2092302985,1987581641,2319318652,2260624322,2134921051,2092302985,1987581641,1899676303,1894091714,1870548552,1870319261,1869427754,1805206571,1758952977,1642878052,1963677063,2133521601,2245010184,2173501005,2207927123,3978031002,2389541124,1879726205,2727291480,3623511233,2661556743,2633837963,2595789234,2230846792,2009056877,1971905563,1969633980,1933422755,1903308911,1894398484,1890247902,1853365314,1750234517,1737101950,1617388753,1185998215,2513548057,1762899240,2177687350,1952855363,2285075482,2976209124,1917584952,1881802672,1881408081,2317103904,1958947941,2208261510,1917702363,1958640707,1914153043,2957523863,2454730604,2433283973,1958947941,2208261510,1917702363,1958640707,1914153043,2957523863,2454730604,2433283973,2165533932,2144194072,2117287540,2088280011,2085866340,2081669003,2055454935,1966982545,1939036167,1937830952,3133722023,2583747784,1989662621,1984426422,1753124895,1747253292,1250446213,2012287251,2117499410,2282994562,3159760931,2968974064,2889443433,2669953692,2619686517,2589233214,2432659807,2280589377,3159760931,2968974064,2889443433,2669953692,2619686517,2589233214,2432659807,2280589377,2238290462,2187813125,2168975750,2115810073,2103000922,2099912194,2055272883,2014616527,1994586331,1973255963,2087225787,2066438833,2301417814,2160550392,2174844835,1734320375,2103455560,1990785483,1894874085,1936691420,1939427513,1998285922,2069613417,2047853910,1987687935,1897509237,1788900995,1901391433,3190711415,3176146945,1927833345,1803760681,1738148865,1728692377,1793559072,1645755752,1768858830,1345619323,1747441271,1724364702,1726053657,1758139543,1277625082,1853807285,1817908994,1830574844,3091043627,2217514004,1727058361,1277625082,1853807285,1817908994,1830574844,3091043627,2217514004,1727058361,1743842865,1658495591,1757508947,2707426697,2120872877,2103467460,2025837655,1950060761,1937770663,1886159462,1879678797,1876531607,1863472887,1797930990,1793653954,1769238195,1747266352,1746269723,1743193244,1736820505,1733320694,1731856361,1728916003,1728533567,]

for uid in uids:
    crawl_person_infos(uid)

    crawl_weibo_datas(uid)
    time.sleep(11)

