from tasks.user import crawl_person_infos
from tasks.home import crawl_weibo_datas
import time

# 混合
uids = [1591615765,1385567445,1923329433,1708160432,1831626537,1844014091,2784392294,2176169400,1773994541,1749003580,6387633952,6044420968,5896780764,5048838960,3995188226,2975237840,2377461013,2340633981,1974340023,1966450172,1965770422,1945485042,1916899237,1912238547,1903789822,1903625763,1885225302,1882832151,1816666313,1773861023,1750984664,1748574830,1692525591,1686725042,1672672743,1658921165,1649180660,1640435674,1561172833,1390699371,1283637485,1064778047,1881627834,5502047317,1725928727,2330523710,1780765022,2330523710,1780765022,1875255893,2532625997,3554773315,1739751127,1715197534,1884525652,1624935747,1548665133,1497549430,3239983994,1741737511,1539889705,6520299488,6091964152,3222851322,2692198921,2474184497,2087589765,2082193667,2079108590,1981344402,1945041473,1931267387,1921174312,1914696571,1913416102,1913099603,1884769567,1878400020,1810382930,1804129244,1777532127,1774453797,1765385540,1759998851,1741045910,1741045910,1708705071,1649434795,1621160261,1482090350,1262429544,1072671191,1778402794,6624452545,6573676152,2864728800,1939378630,1929874647,1900663142,1822038145,1742638357,1737930424,1796269397,2258892540,1495493433,2483921254,2367003454,2307791283,1683407537,1874143807,1910366632,1743021332,2538203313,2687650775,6322740243,6080876568,5975390352,5678640255,5392237610,5133947393,5081463497,3909375213,2809452042,2341903437,2265209384,2248012160,2101105390,2096623060,2084586665,2077627203,2004668453,1987083930,1984473287,1972815231,1963921501,1955216385,1935171695,1911178913,1906057667,1903629177,1897850975,1895169577,1868733390,1866186067,1848780924,1832201225,1779068192,1773401234,1772140502,1760796355,1750446441,1749899933,1749247267,1748770082,1665930990,1644188945,1454856970,1439100767,1438914670,1429894011,1438330775,1717421093,1767979002,6602856585,1082618390,1769862104,1666446841,2264861274,1096144964,2128114692,1667040054,1796583611,5760316725,5057648451,2061634753,2037555817,2120189375,5883875766,6062061118,1826525115,1971071013,2629054433,2569255762,1705586414,1954029575,2211692642,1225875705,6273314994,1737807023,2424951880,6100913448,1745983587,2195873072,5261392099,2047411571,1733823195,1678615953,5294283848,1909234250,2177128480,2082479713,1788074264,3192377322,1658038343,1748276422,2574729682,1889800447,2429851157,6274830968,5669948350,2968917401,2473139527,1747020855,6085439925,1927470502,1072114674,1801908833,1892202445,1423932953,2740375731,2523765783,2509835342,1570759485,1724535233,2263829824,1736612734,1957630834,2857946477,2001422967,1758018645,2219045034,1917866641,1747057674,2189301164,2450381973,2845085123,1800453514,2097015407,5878380689,2232979462,1661871063,1744989472,1063939965,1892760563,2188229602,3068271535,1270464685,3242286462,7032594159,2948938582,2783974057,2617603100,2902711624,2432174463,1787243924,2145208437,3803326295,6583442048,2414887902,1799955642,3760051057,1800506271,2814622677,3713447407,6296747031,5991624834,1969037323,2848055390,5402297510,2654427672,1233302050,5591571830,2653757423,3052979275,1868411382,2083250041,2997398224,2596830171,1641497180,5588886106,2098444715,1684215787,1865782687,2426761597,2442057760,2010620517,1885264344,5401297913,1974962223,3775517555,5208947987,1993284787,2313588903,2132702877,1765638243,3743342005,1945792555,2715439555,2015086945,1998151800,5111312381,1380437732,5430376657,2415286217,1403493257,6545166468,2288151154,1953889467,2091637207,1964197774,1943260757,2280643100,1853278731,3446918834,2613074751,2623298963,2469250724,5399608881,5272060572,1911584980,2503237427,1778405573,2124852567,1925150367,2911679892,6651123467,6235618736,2128010293,1890365822,2664016443,2603619372,2386031194,1946162521,1746929851,1743412251,1915228124,3885566230,2284716240,5490363514,2629911984,2967043450,1969612743,2874137654,1773042332,1621807562,5677879550,5677879550,2114307094,3367087110,2392506422,2275124000,2060203757,1991483960,2067929917,2137814575,2185636354,1993293327,5171760236,2239885934,1986323503,5025858701,3188701740,2278427752,1684186641,1879084542,1563736384,2012462425,5447091712,2232007645,1908324701,1768463140,1848596804,2263607023,1808235740,1897490170,2336468583,1960864173,5024348861,1940530013,5281228416,3514908287,2692072071,2184616162,6502787752,2198659273,1796814661,2704477012,3225343105,2828176024,2827913884,1626846692,5318347605,5274556885,2664871933,2302339522,1921488123,2166219740,1865352912,1882038785,3039476742,1766800491,1972697855,6019447155,1998767641,1873621425,2303890284,2804245132,]

for uid in uids:
    crawl_weibo_datas(uid)
    time.sleep(11)

