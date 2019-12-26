from tasks.user import crawl_person_infos
from tasks.home import crawl_weibo_datas
import time

# 全部（原创+转发）首页
uids = [1930884353,3582228124,1719559670,1611754727,2187103453,5091392475,1803744462,3833744132,2965138602,1767608354,5657476588,1646724250,3535176134,2185074745,2384889987,5386161998,1692776075,3682999864,2077660973,1758712697,1826525115,1801613592,1773783120,3002769550,1713884881,1865978764,2648060735,2519989755,2297209342,1922767555,7282449375,2105289787,2097881461,1731255084,1926488794,2049988057,1377603885,2461317097,2445520177,1053527323,1660514462,1882368101,1424742943,2488599352,1864799272,1972427375,2057820462,1489274942,2401810165,1750889703,2802828740,6510056771,2735794504,6019447155,2519743935,5081429204,5672139983,3885405580,3481171611,2256845713,1641097943,3119587257,2234107201,3401037174,2429191657,5637867804,2239795094,2446972752,1791715410,1834186073,1950085560,1980237443,3934143781,1737274971,6014266561,2918594133,5070188893,2038227185,1059793480,1916349027,6867301016,1819624211,3104868484,2158791494,2155342182,2295382050,6363058686,2036825147,1504205001,2993479121,2035438490,1883771101,1847060440,1966142971,2764693167,3387916322,1863727100,2628415803,1778539981,2104636892,1738167003,2167388512,2434795671,1849181695,2198843110,7004513026,2108429087,1992635090,2546228472,1795761910,2171957320,1174780713,2683218211,1768000552,3168387703,2132184550,1778677907,1875432911,1463115244,2470411912,2500397143,2378832057,1405904170,5630529200,2460514315,3177100903,1946962144,5697130861,2083368823,1879073262,2281874014,5683332166,1890203311,2607362421,1740111814,2752310202,5262270732,1071307377,1709472675,2902245391,1343018293,2385864430,2341153571,2010368575,2385169734,3002903101,6452117580,2051413801,2157126010,1734452462,1451368637,1985441664,2472020234,1803327863,6112892003,2724422735,2055318957,7332212156,2867404690,2084640745,2179009731,1717421093,1960560953,2690734411,1749246703,2532889027,1300566840,5620443059,1312392117,1686707184,2131226731,1619591677,3908829913,2190947913,1613873381,1771249781,5647630462,1951800275,1875226515,2709386212,1782541214,6228321446,2181190204,1705464470,1763148880,1738780805,2932569764,6724919404,2000399650,5117400974,1999899003,2185594941,2079950103,2545656532,2167330924,1364364950,2483921254,1776176491,1778923885,5482412062,2713778643,2130671710,1645094924,5721334082,3316785091,2964317964,5985441360,1893016034,5065448624,2862062964,1725938721,2701978040,6444928493,3228885514,2685539857,5394180561,2061519193,1657690037,2372617344,1768338932,1067254393,2682870250,2722933133,1998767641,2813700897,5093102808,2161832380,2177128480,5827943461,1987192105,1903188000,1823330905,2650180921,1992102463,2650158002,1853575050,2200605753,1732350922,6414242568,1912144421,2075210185,2169708532,1719390250,2550260494,3792154461,1910298564,2237161831,1787354710,2209818485,1763390823,1862617163,1148264391,5780720757,2149808584,2958931044,2043863243,2622502001,5883086016,2230154083,2207927794,1942604511,1826659770,2089159387,6296747031,3179478632,2736350464,6591444220,1763249712,2233695067,1727025627,1732234741,2765693323,5736563115,1819588781,1941038663,2130829205,1770586775,2092126274,2122925472,1750742997,1973586095,3951629844,3743750983,2240748163,1655132001,2487583840,1054234800,1986652563,1884898510,5775016590,2716292897,1791629105,1855997930,1884416340,2501484800,2481198817,3161741004,2678109304,1925098691,2734925373,1648558983,2153179540,3188608947,5210612592,5591942504,5572863023,1865429332,3416781040,2964584212,2320308192,2574427814,2649081921,1711791664,3862977149,1870560710,2865920920,1907532175,1746867844,2309065507,1770891923,6029948614,5892474702,1865327042,1961100434,2407281921,2104880740,2184353660,1733773640,3240315634,2692247233,2054243091,2878097892,]

for uid in uids:
    crawl_person_infos(uid)

    crawl_weibo_datas(uid)
    time.sleep(3)


