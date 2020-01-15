import sys
import os
import time
o_path = os.getcwd() # 返回当前工作目录
sys.path.append(o_path) # 添加自己指定的搜索路径

from logger import crawler
from tasks.user import crawl_person_infos

uids = [2063177070,1957867105,1936483514,2180318997,2356364225,2296951390,2477595330,2209046154,1950360182,2067468482,2616504913,1942548703,2155016511,2438992580,2166184257,2813950722,2295821953,2097263201,1741439790,6177752088,2605100632,2439118222,2067222134,2046931303,1973935113,1948227363,2079674184,2165728411,2297483077,2121354665,1954300121,2082478903,2169405287,2306322141,1975093855,2259094673,2611857352,2366924582,2773921277,2131481943,2499581502,1975484804,6254603740,2291725934,1703839015,2703776011,2381658192,2269118474,2546366450,3965883120,3154746134,2171875213,2316010971,2287849763,1960489934,6721510253,2616828821,2117280303,2881527000,2370652853,2367669283,2145014527,2130157881,2378930830,2327024344,3268757737,2131434952,2833243154,2672729050,2643784820,2527061300,2132743141,2697275173,1681128137,2231026283,2261644870,1813900330,2486721240,2409257954,2130221383,1314643732,2372935337,3987346468,2479954457,2380962432,2132532835,1323826432,2230795207,1883049447,5171995411,2992833490,2132405010,2113630280,2723507665,7164756288,2411234652,2392674554,1415758363,2430024834,2301692590,2140621495,1772607504,3128031171,2798849305,2349403295,2308048241,2256376942,2156032410,2133312344,2131306831,2258272014,2432328665,2292302763,2247671214,2879159184,2207836822,2512574222,2299642821,2246296700,2240840782,2192187277,3064054751,2728793684,2670900355,2635886645,2619429072,2579224654,2546796630,2391820624,2377325265,2342543555,2306296375,2237986264,2205769851,2477542872,2170714223,2402959515,2683179505,2651109923,2529422532,2472419804,2424322405,2402128725,2393652545,2193056533,2267192884,2294559062,2641904202,2394637674,2241413275,2382647912,2617116104,2507768582,2495306912,2403740891,2394420021,2317689095,2297730835,2234055633,2134216271,1762157932,2288160142,2164692190,2705567971,2164294034,2129100754,2891923700,2646829311,2579316577,2450838361,2340044917,2330579004,2317561905,2295568192,2232076463,2188280034,2130678445,2105508200,1958990610,3652551967,2626551705,2296965287,2151676097,2497702712,2854240921,2647496527,6135079823,2646472605,2559435894,2517376780,2483441440,2373236291,2370467901,2315104355,2255360782,2187627680,2179165992,2152682365,2106223685,2099725164,2383868833,2600259491,2329054951,2363072565,2168993704,2390183832,5272034834,5271821400,5271750977,3250323991,2894886875,2830082184,2792416740,2600356764,2501652425,2448249982,2431416380,2401457141,2373585287,2361005474,2340733955,2290756552,2212754944,2152261374,2130415523,2837361600,2487424197,2431865022,2391616452,2353696280,2244685565,2159510861,2209953292,2496550581,2304554360,2393019391,2087216603,2139077825,2254514820,5273048721,2730916190,2703169774,2415932520,2413159111,2403968614,2398284524,2319064037,2298842091,2283327433,2248361570,2217533955,2174344870,2123987665,2102320711,1840851325,2656008583,3097352887,2342692245,2425640884,5271832890,2627612065,2551867362,2549911682,2539402623,2495825990,2478912404,2457268670,2432117952,2321516794,2319957322,2257976370,2256148605,2255674551,2231069334,2186797553,2178120291,2175155697,2150808347,2120467505,2104597944,5571383340,5271787001,2541998722,2241327602,2119338040,2392779657,2862842780,2255408220,5273040081,5272023545,3334231614,2876176584,2786897194,2342967021,2324672520,2315941755,2296536867,2285019772,2219978695,2212912632,2165992231,2132434632,2598791903,2787338350,3063271703,2205753243,2081353275,3262357500,2787387840,2780696830,2659526783,2658730580,2472416137,2420558504,2328762197,2303128810,2281761035,2150359382,2077500245,2263418284,2265357107,2261633874,5542105340,5474468441,3199636604,2686785531,2612711227,2478442690,2469699372,2449877082,2414578875,2372251083,2356188482,2354573217,2340291280,2316298360,2315641680,2310367173,2251690512,2230442063,2150583064,2149705523,2135618873,2109968580,1994112655,1784401533,5271748138,2381460181,2294315090,2908791910,2422883564,2279311795,2119124021,2846243274,2714980054,2437100534,2319483204,2313841701,2643587484,6530389179,5695725823,3409176370,2919567193,2821031373,2684960270,2647829702,2628643603,2586399861,2572322554,2491599064,2488977063,2446518502,2445089781,2422508412,2410159405,2402143712,2400781062,2389611843,2376736102,2352695334,2350125814,2301613327,2291051472,2290340530,2253878964,2191102040,2096044035,2977579454,2403508674,2407411852,2241621360,3242908261,2431721065,2395210133,6352196135,5271570508,2770968251,2734895203,2711647483,2704601005,2651339103,2638937141,2638835223,2621528333,2447935097,2441821262,2421889487,2417568432,2402307623,2365756147,2343052243,2318168871,2115466091,2050955710,2032188521,2012166355,1952313817,1930346505,1913093627,1858770340,1851248552,1838251324,1824910757,1778385734,1777904804,1776836004,1732154172,1711088544,1570760147,1347071722,1170576223,1059513360,1660489165,2059200395,1794603252,1357967134,1180814321,1700328410,1719465397,1727987163,1349127603,1778078270,1778166571,2006209495,1798093607,1883122000,2088500747,2057660150,2053987313,2018562882,2017489447,1957276487,1911833485,1898053232,1878869344,1866879434,1863737453,1858610732,1835541532,1800041375,1798567512,1793465627,1787072977,1777206342,1777038782,1772895257,1750960817,1732417047,1728052781,1727951942,1693107335,1579753777,1576519165,1503003783,1354244665,1241706713,1188238367,1024371592,1011765781,1000187380,1751782201,1225653417,1654495502,1349126510,2002560071,1957215200,1844887110,1777745423,1776052215,1957803892,2039897605,2001614104,1950899671,1914005891,1893865840,1842026442,1812087531,1779460652,1778369867,1778226024,1778152930,1777959732,1777533772,1775808124,1762599820,1761197552,1746800027,1743817375,1648732537,1223121233,2004332361,1952020290,1652303805,1236697225,2055629457,1725425393,1847497033,1703629142,1834326570,1888828232,1850623505,1344758823,1776789013,1709707757,1778318865,1776802142,2074921453,2040909167,2019165131,1985031600,1911966062,1900440300,1880447004,1874080983,1870517871,1818669053,1785359285,1777777632,1733008185,1660982490,1636236241,1600562883,1588292623,1460518041,1258235024,1109263043,1986791101,1775026361,1792311365,1826846654,1735893155,1837331785,1588452765,1735368632,2825772081,2119864302,1718930970,2106955014,2105200977,2099249251,2095774895,2059249193,2006321941,1918933634,1908440831,1884229764,1875852825,1859161920,1847808442,1828181751,1820640877,1774015461,1727186594,1612530733,1372113632,1287231364,1271471777,1092112802,1046685425,1780400633,1748829752,1738211590,1703477922,1222704157,1172624930,2109921251,1872459511,1869776271,1728130664,1308359705,2419439852,2146779537,1990064023,1923414951,1906304963,1855603562,1775599907,1770073423,1769221505,1689155094,1685966553,1683948743,1642215750,1568619675,1421697704,1204821250,1157149163,1878653071,1888850121,1977526903,1851134524,1837535495,1636429870,1986678610,3159219692,2879329724,2794201912,2745978731,2015851923,1961095061,1956604713,1944608717,1913523431,1876997754,1788740477,1740575357,1685037532,1674204760,1553706427,1158177577,1970828991,1876774133,1804449162,1661944783,2071972845,1967365475,1427195981,1739931502,2735832512,2675052097,2650032132,2512119961,2436545610,2346438205,2057713781,2004541591,2003954010,1985616933,1980767397,1951120153,1946900220,1926792931,1915397650,1898059610,1877328472,1876047915,1830707300,1728126557,1645262897,1607016897,1589927321,1500428255,1444542025,1191059502,1755350891,1986924074,1736812974,1612363874,2093462811,1427077385,2098885975,2004862725,1999612553,1975261220,1955246033,1899191447,1883176564,1878297963,1868568133,1835523444,1800800044,1705968513,1698146477,1656128961,1649865913,1605558787,1537712111,1480317304,1464720222,1393582164,1273382381,1053689404,1729604932,1760159333,1976635141,1948044287,1282919993,1960725521,2953625930,2809354032,2780962815,2703329511,1705579077,2097790461,2709176442,2696845865,2345530761,2493973960,1293263543,1914953742,2915942317,2124292194,2497302284,1966810393,2809162174,2135692935,2049999261,2872191400,2295337760,2183503090,2525408484,2255867594,2245050760,1564328771,1956941877,2001537691,2034914831,1912658627,2306246963,2218960174,1893916113,1753053280,1676431424,2480341362,2100971647,2097321093,2183059570,2159380595,1960242422,2625588473,1938543361,2109938224,2304523264,2019354435,2285228413,2512552124,2107021282,1935814277,1988743577,1931268895,2257687564,2655166753,2813773180,2195266252,2146671943,2041348803,2033710543,1990115564,1827433652,2363032372,2104582173,2165371840,2436059911,3225623207,1880734892,2703764007,1913599107,2694245951,2023296035,1707405694,2173113734,2031791697,2038540180,2622950392,2269193653,2296452362,2126440492,2214933680,2366108822,2187249561,2048896623,1985253855,1918619787,1780481510,2823430041,2413640330,2390342623,2360251557,2319614020,2287081660,2121649577,2119447102,2069789485,2001789655,1934224882,1912187667,1986800191,2010657821,2393502837,2285122020,2372128380,1944219925,5433711551,2356700582,2197310544,2170529773,1997999031,2538659092,1962213682,1919840867,1954839891,2304889967,2186364034,2096530635,2287819482,2357005704,1966583964,2321470924,2127533935,2133607204,2182371887,2073557991,3810701085,2493870582,2381024410,2354154002,2206514274,2155406043,2138151373,2128170953,2118268610,2056670212,1928665555,2454737634,2048416734,2150869982,2142557365,2615849205,2470041674,2837767622,2739922121,1172179370,2367031550,2207680123,5104572616,2732787201,2006320157,2675229001,2591436770,2353622587,2293581474,1976101422,3563531320,2172858992,2392055893,2277361445,2170388342,2164736830,2162658620,2158506402,2135062697,2095098057,2087919181,2064986693,2007343581,1988132957,1975130427,1964661923,1922402904,1921017957,2268294641,1727684092,2114292654,2366049752,2085353835,2873100952,2155311524,2653913660,2880860570,2098510987,2037374795,3199623502,2096968782,2438029600,2717494053,2024364470,1663286750,2421427024,1644476531,2953346322,2379817114,1984686965,1917878520,1869091650,1855323011,1829843905,1797355592,1724017797,1667703735,1662792733,1626249705,1625457987,1852254504,1888904997,1893385044,1654922775,1901051185,1836680300,1248410170,1770369072,1834500302,1700719313,1506018721,1824851094,2367328183,2190305767,2061930995,1909179827,1883938991,1799108671,1777612422,1672599341,1285518900,2084603451,1563578383,1752022783,1965366563,2816686300,1883400090,1757440057,2181269552,1845110523,2480950182,1761219424,1964163423,1503870981,3174170730,2016031243,2137032950,1893537182,1865422570,1861633642,1824492895,1806934360,1749280140,1660376374,1576723424,1428820687,1397905011,1343278884,1140575507,1149171022,1871320450,1895780483,1765664980,1869527060,1900610571,1864844804,1359568145,1818204954,1762854422,1686088774,1622761300,1740297505,1659254822,1358012521,1879151914,1851054650,1776285725,1583632231,1948102931,1901318497,1893913410,1890459985,1878757694,1876438742,1864570433,1862284782,1840753682,1850994315,1716378943,1678081787,1429263320,1917587160,1741587930,1677504750,1861917820,1823584394,1731055821,1729081824,1879373004,1402640187,1736275372,1633702265,1841393675,1893356622,1619079237,1993013457,1975144453,1932278173,1920876410,1898619090,1877709521,1874641312,1871407032,1863998803,1853141787,1852443071,1800503122,1789577397,1784004871,1777175323,1772018520,1767986202,1605077160,1419843947,1407757747,1261331565,1678178121,2110415777,3959639975,1590973634,1805392294,2806586020,1904959505,1269544125,1801979963,1924439014,2175399114,2631656612,1300792480,2670670820,2175620655,2537995542,2345387884,2106932871,2002679043,2539078725,2076757905,2096444057,3836298963,2575229860,2089105121,5906225068,5348623284,2898508622,2572123103,2687512493,2924814537,2169193683,2023726647,2108029922,3214862263,2984528473,2345539597,2080340584,1962734111,2373071410,2278514004,2418633147,2162017730,3298414465,2285722723,2358631824,2186210467,2186025982,2282195124,2280620113,2186054853,2098412437,3083845082,1624896360,2609891275,1999605745,2747657702,2399360434,5816495337,2644688120,2543813665,2427669952,2394794335,2312124621,2280543482,2112603127,2054347895,2008115565,2184059110,2672856383,2516944782,1921503427,1874049353,2318788323,2181227540,2028596090,1914291891,2272025771,1946892790,2166443620,2058224132,2057246984,2038554021,2002604967,1969955354,1943895057,2460397982,2185032675,1912055393,2346436364,2006548552,2739987043,1958100981,1972702480,1919133145,5633571168,5082156115,2812875354,2655997732,2607447012,2561414983,2462811224,2312124464,2169770687,2106844820,2073272537,2009289491,2756727605,2157966115,2710791415,2303580984,2236704513,2164660633,2288356042,3863581994,2656145063,2315838702,2098513817,2270991042,2736837194,3781763132,1251018534,1969865331,1981401761,2491752202,2456844740,2119928315,1969622091,2417437912,2819586413,2174822923,2200789622,1735861491,2553076993,2642366861,1928121627,1269785690,3194232323,1978371031,2162569057,2129212790,5528543904,3177903170,2940993752,2808031012,2644093323,2571591072,2540650170,2391824780,2271069537,2238436127,2219910695,2213136200,2016152935,2012484440,2007094932,1992822144,1988457303,1977001397,1719868981,1678559727,2037300463,1963666635,1937692464,2180296120,2584856911,2724673041,1959989851,1664990314,2014605821,1989966863,2696502713,3869681901,2713576912,2306252767,2206501900,2932803213,3965708970,1937030242,1933164331,3315728173,2001373860,1917172783,1905567082,1964730435,2703706707,1675510784,1660148023,2385517521,2045400224,1787695524,1854342345,1858099290,1881255880,1713483895,1852434662,1845836260,1906712200,1951778371,1916744810,1867665734,1563401082,1663288973,1767652314,1539145741,1964890534,1869760485,1401487300,1846967844,1939452614,1929965201,1802067882,1756721833,1899073754,1769166900,1894743451,1573059015,1850391192,1899285245,1735683030,1785655484,1915470020,1915134001,1912385781,1884247620,1855169961,1849044784,1848610904,1816735380,1811920937,1791249924,1714308447,1657153304,1644102342,1504816667,1353341585,1749895090,2401826377,2200857525,2080666055,1560455913,2139051025,1781442394,2473221874,1774348002,2271124994,2027328464,2315479785,2047287627,1788870765,1860414010,1757306631,1895177645,1847169391,1562446144,1840665171,1774584197,1747096601,1892783330,1988537455,1928375925,1917003462,1890764510,1846189320,1807866284,1737582853,1873321942,1904768764,1725817647,1857052190,1804430287,1694765642,1342211380,1879473250,1729568220,1762107005,1795671913,1887161077,1740915520,1648013975,1780920931,1762427280,1340395787,1848777325,1318069910,5822351314,2994181674,2368831492,2351811427,2247106631,2102205634,2087399957,2078484937,2032912571,1936492937,1900462752,1864622455,1828811143,1806923530,1797133994,1775592450,1772278353,1769769623,1763076900,1741317477,1561783323,1465734945,1221335653,3165258370,1810306310,1641511401,1723834294,2101802157,1658783931,1996096817,1661798632,1809924754,1700106931,1279672982,1763164910,1776140823,1594353893,1881543420,1888148394,1748029597,1890381690,1882937930,1873670023,1318802387,1938567322,1887790220,1772185862,1768409950,1892374032,1891286957,1798592003,1282401261,1748003014,1790228804,1488379987,1267770074,1861891221,1778157035,1802714345,2144350375,1729465501,1707052335,2093287432,2340295032,2793620222,2718418593,2553171361,2518435510,2433167574,2279098032,2276179044,2258556927,2097999450,2047704311,2011089435,1984771641,1982482942,1980265617,1975470753,1972145511,1966497353,1947097547,1914794942,1838119627,1821205022,1805320164,1791162681,1777156782,1729033154,1653197472,1645204192,1620059277,]

count = 0
for uid in uids:
    crawl_person_infos(uid)
    count += 1
    crawler.info("count:" + str(count))
    time.sleep(1)