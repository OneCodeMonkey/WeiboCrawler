import sys
import os
import time
o_path = os.getcwd() # 返回当前工作目录
sys.path.append(o_path) # 添加自己指定的搜索路径

from logger import crawler
from tasks.user import crawl_person_infos

uids = [1805042910,1955552294,2050211252,1833885582,2305752954,2210686562,2144304793,1926480397,1950180205,1980569737,2130796823,1794472263,1988258907,1787156631,1892310945,1922379873,2415301475,1867038861,2819799342,2692127345,2599119884,2598491690,2479613881,2449917480,2438782611,2291295492,2282192550,2186262132,2105018747,1840763312,1838326605,1810018800,1767508100,1745703711,1784027405,1920234935,1788226004,1771951317,2092372442,1940434403,2471465254,2592075250,2172337983,1790510565,1924435632,2285228413,1826619443,2087821267,2280098922,2035516490,1848955507,1834746702,1950585292,1892873474,1840615627,1976029565,1944672773,1745756227,1940931342,1844223730,2161650180,2061496301,2019430247,2008468681,2008117425,1960675161,1939504433,1927347917,1956292925,1877308520,2107021282,2139261550,2230632123,1771119447,1803656150,2083194471,1668606230,1951066144,2403257155,2117134290,3312191935,2427409432,2336939441,2540771280,2282946707,2124499353,2682526244,2686239873,2046946251,2145849811,2137032950,1786771521,1864244004,1929250697,2274500982,1827146882,2002799211,2308994702,2001003377,1932749550,2806053243,1915090890,1782783451,1783057102,1844813762,2552042477,2163962201,1954580040,2696209482,2152389960,2212260770,1871064555,1868145225,1686378553,2164775301,1845814262,1835348865,1874854237,1998203590,1945108982,2098508597,1864292622,1767721950,1981771885,1896502027,2155366870,1784508361,1966986761,1975341740,2149467912,2403672695,1797428943,1966641261,1918390225,1907197607,1892575181,1822736605,1804404062,1800345407,1709562457,1709607195,1638911563,1920096485,2463196072,1781197681,2374016827,3179621904,2372128380,2983674592,1888747871,2314661537,2247580564,2097119014,1937657053,2023538651,1828655404,1773787842,1734122504,2092100331,1687197112,1762128910,1850061697,1838598044,1808672232,1770252390,2954161690,2815452854,2639477950,2628662125,2468662772,2463730943,2458693442,2427810552,2390342623,2371675672,2354729820,2296172651,2287081660,2285138053,2215279882,2138865924,2131265001,2012233473,2001789655,1997755631,3206551791,2422765592,2693511987,2476870225,2709642547,2636503083,6399355707,5199993985,5578904147,2360657154,2372309510,1973129855,5904588961,3880640708,3220880985,2984705771,2911571120,2878632460,2857073902,2819370043,2684756685,2681601452,2670344163,2647782307,2457647974,2439539304,2356117394,2002576503,6209160489,2471879642,3662526142,2378938771,2364925811,2849014397,2771664437,1973125615,5338111901,2306585954,1944776310,1863978900,1778555010,1660657652,5266553917,2706887552,2675890511,2188478664,2425718154,2319726524,1824621230,2371241644,1871836107,2577991143,2186593141,3542656710,2116378141,2296573794,1626108992,1804162347,1849705431,2351769253,1778312475,2108025954,1913129190,2305327401,3137299671,3518999795,2063704722,2019692953,2158404654,2322602950,1950886271,1942945233,1868852075,2044182632,1955818990,1848998631,1976887197,1777322717,2205879032,1787880073,1962198835,2778237515,2186054853,1785132497,1807606932,2190936094,1905680570,1791792075,1762107210,2254559410,2204316020,1936083113,1873162454,1820727072,2589903397,2461407933,2835293730,2642625412,2813152351,3304397314,2676724631,3794365357,2708188267,3579668277,2167322787,2100851125,2129072584,2378757145,2218797501,2215181203,2455943363,2491552392,2261859235,2817878920,2250096514,2375433604,3747194363,2570618201,1794596551,3968732484,2733493182,1935130794,3186093190,2389691992,2474860732,2440819204,3867629789,3192926570,2458973515,2286588712,1934503173,1783462391,1653653417,1646608551,2411863624,3310280921,2620803967,2795936141,2633686625,2743655320,5335366957,2416206300,1736356153,6715291465,3511782655,3178469135,3167310734,2944643007,2850646220,2944007662,2450016504,2449530295,2729183720,2265427394,1939797683,1839351215,3378688204,5242384328,2870677124,2419491444,2819389044,1960197147,2836808770,2679016824,1951704931,1782577190,2855298922,2657598900,1640508370,2291524740,2244264074,2821778204,2326512140,2724021700,2643616480,2501820694,2499410191,5128379431,3816317683,2874025085,2680331433,2494599115,2450259884,2005049537,1791843525,2644966394,2678653221,3170319741,2881946682,2706756114,3178010330,2543595472,2557972720,2324498863,2294989074,2358210360,2691453343,2705638493,2536883201,2350811712,2436257322,1609361932,2308818505,2547909012,1960800341,2743881634,2846268354,2646807803,1988608307,2684181345,2657815740,3673059192,2869610024,2617513074,2437471520,2396812027,2405804800,2430310875,2696572471,2550639060,2671200871,2265695192,2652302861,3170893400,2946217105,2802214105,2449382742,6318845904,3951239865,3816266677,3566463777,3208795514,3016712593,2947455952,2925820145,2787619350,2726850024,2723422482,2712724035,2691780502,2656740321,2656534314,2546473780,2407977843,2391902602,2390510381,2385797270,3197474834,2036403352,1863004620,2238456194,1942682833,2209323874,2124540395,2485168201,2643796791,2810034591,1886041831,1919405580,2210903565,3212095597,2285908683,1935239943,2108439073,1771010597,2487753240,2814720391,2957931270,2328408904,1782849827,2325354081,2335374964,2041371020,1935598961,1785919601,1808683672,2298169361,3453899670,1980491941,2476833234,2034398794,2012298311,2232232957,2091525857,2272664804,1805099030,5094674428,2862401354,2130926773,2033843417,2562071647,2483869050,2456673040,2389317260,2365487835,2296672884,2180569382,2135919237,1986975283,1915371264,1913452115,1979533164,2496542214,2448192417,2348856930,2276868734,2268169820,2120454821,2096325402,2063928263,2014017372,1970977581,1892897547,1883810802,1880590480,1824967947,1788273112,1890321320,2277174324,2135606122,1846845542,2130681783,2273430472,1794522020,2267807402,1669377652,1976808941,2233626341,2184214070,2318911374,2019898353,2369549893,2247214962,1748361781,1863677004,1814784085,2257158450,2030715681,2460400892,2165919052,2043348945,2182313220,2463081885,3158667803,3089384273,2766849500,2698078343,2678646310,2629120823,2567976490,2548344551,2538328840,2497858003,2426922345,2422690402,2353258110,2323097867,2276412205,2274708834,2265588374,2254432274,1839486301,2583621120,2605463205,2584130471,2115250042,1933440663,2117257912,1953670545,1947214447,5984379011,1839351563,1886328664,2717399737,2294657040,2135166634,1950241225,2214779775,2884228933,2109505082,2387489932,1784942444,2120262917,1839461115,2354587610,2277691772,1870229711,1692884433,2111852473,1985243377,1752628494,2168754605,2165835362,1790267785,2321908132,2302604372,2295577183,2280746954,2279836940,2279090504,2243003425,2211450563,2192339302,2160392712,2107828100,2098645481,2030962233,1985012921,1980272885,1975049401,1958976425,1944792680,3197699283,2693042681,3960102802,3787667981,2317398557,2428536912,2410822717,2279334341,2804341212,2539753245,2576900860,2664285901,2708391955,2493087605,2390837462,2332679640,2387093440,2396356475,2343770984,2294791464,2240435187,2423280071,2546507124,3177233652,3138897352,2806925882,2373812555,2325161790,1970238491,2822986550,2603971990,2949020692,2528897381,2322801882,2485934220,2529795885,2629420847,1766391730,2860316803,3805746030,2330281470,3225880745,2210917184,3481918603,2543645144,1742235077,1308441915,2328079190,2290870314,2626833125,2432733001,2581129340,2399423067,2309984283,2330365960,2304363800,2423773703,2449820400,5881839084,2321049207,2369988641,5545205982,2314979064,2784925470,2346566191,2310669560,2207944673,2473582195,2707198522,2315843883,2878319194,2236164367,2267858100,2648851033,2517411044,2306375244,2429370985,2422317764,2308670082,2432170214,2178599432,2336768690,2672176515,2624201627,2543699552,2528897341,2407731595,2389599191,2371047460,2363619300,2354854162,2336847914,2302595540,2213361421,2197788154,2190382633,2034554213,1907643095,1882915094,1641944575,2592213035,2301360291,1959092571,2121531760,2254199412,1776560062,1831865560,1869095681,2033603384,1808693262,2120585420,2090500871,1896050407,1855016904,2488078210,1892297310,1772718637,2038628742,1827873724,1761736581,1728060073,1781898267,1828682844,1759425195,2473355130,2691696575,1952455945,2622990291,2396393217,1921698997,1889502514,1768115275,5313206969,2159283607,2165753940,1839560723,2869520464,2275820510,3009979343,2375932690,5157753417,2153294370,2422903742,2370294060,2322306587,2275614965,2255966192,2130428124,2118143803,2035599493,2029140857,2001320731,1839883260,1836966262,1794354384,1782010834,2140690070,2864387732,2091672743,2061400815,2191987687,1862340261,1809053442,2690860572,1861451852,2231798807,2447720172,1977516262,1876003742,2535722775,2393622464,2316872183,2298867322,2281552954,2152690990,2120873572,2084828633,2069363751,2063242011,2015119844,1937996625,1765824660,1634212125,2104194743,1946203905,2131225332,2417075111,2499161962,2481243637,2382372532,2705911441,2871281724,2516097910,5342070509,3744073125,2322045224,2482878731,2495331694,1940707241,2711939072,2374176505,1775226855,2386957060,1903511273,3160374304,2714855281,2464953390,2268603532,2833613520,3654488432,2891392161,2834182753,2834058652,2813225514,2476369375,2495383941,3004079934,2649413492,2310651894,2378189283,2254402955,3037370201,3285742365,2705722163,2432083461,3179728922,2262842464,2249966390,2691830513,2670878600,5681432636,2870047164,2583933474,2348041880,5131852820,3855827836,3481907591,2757924062,5081581950,2497858473,2476338940,2329740742,2938525402,3211932291,2371279323,2709711330,2313435865,2827794352,2307177380,6011107349,3196733287,2973853962,2865477874,2639416101,2504903037,2496894684,2346484624,2316201775,1963499015,1784360535,1782776837,2455620665,2690685114,2520176160,3178189263,2403720280,2363696567,2214353530,3833111365,2775376515,2671130111,2669606580,2604165541,3612666380,2307596033,2854467800,2240155984,2587571567,5095071498,3271244811,3218963501,3170747862,3167417010,3046658001,2906487023,2775324123,2689850073,2567729284,2349530380,2395710890,3071790290,2629544030,3968807105,3367506664,2957244664,2873044070,2781298150,2690985712,2690982042,2601205323,2360732062,2255180467,1942225054,2603067801,2690976154,2289264214,3227438602,2750516363,5402901638,2360096262,3175793374,2378761710,2290850070,2290334833,2886583462,2559491537,2369344862,3830110211,2466866530,2402251044,2286643750,5644886724,3341540434,3031003323,2856833012,2693511253,2688181693,2301481152,2939430951,2472057142,2431510390,3837118987,3172837900,3087019961,3070156061,2988969810,2980526701,2921308195,2837417064,2530035105,2357260042,2344675403,2370254613,2819491944,2883809864,2503396233,2366928204,2318275442,3860076577,5610410225,2687342474,2686767312,6140049258,5077867835,3199989584,1854410871,3121812365,2290065645,2757944681,2510879281,2447057154,2527353945,2349588342,2337036612,2849064250,3008010667,2047902940,6039101447,3977997846,3518595612,3306149657,2438402620,2375880543,2678363401,2553197437,2857457560,2987979860,2718676431,2706604643,2519500921,2515390115,5292254017,5195709499,2691772133,2650033411,2442642285,2431886760,3239246364,2551060633,2187872910,1863024474,3807891234,3524443201,2879715312,1841507430,3659411605,3249268694,2997601497,2881129162,6280655662,2244173044,2384068783,3695612003,2947735584,2490286092,2413712293,6593536443,3315117062,2403500181,2433928937,2720217564,6006121280,2765760165,2432405792,3248950840,3155771380,2776755880,2759405427,2643540093,2454928081,5224546188,3752706043,2518818030,2558319421,3453334800,2609626813,2863869780,2863928691,2685611242,2643309264,2578448197,1973520693,1968193133,1832502374,1784904130,1658803977,1585958890,1634955690,2405290267,2872710990,2270620912,1768001295,5629178775,2529548284,1938454730,1768700242,2514058577,2887521502,2763722760,2612118257,1793529805,3186554225,2977525742,2803169445,2538407510,2482183761,2450317927,2449703681,3085123957,2402772353,2385190497,2127152521,2041766957,5752769561,6402155909,5625627535,3295108521,2803496587,2543144594,2517437330,2411506241,2400800830,2390513532,2254301810,2137643220,2090461237,1771372371,5628304314,5151096410,3777291423,2940740321,2828826735,2737660391,2262157492,2063227051,1700352595,3164095114,2501025947,2491729643,2284923660,2635166887,2307547852,1606993063,5040223262,3537079792,3089537970,2827451412,2694094900,2687262370,2628796543,2604967844,2598168807,2455703710,2424080521,2416509623,1900784294,2455662244,2669790817,2557172302,1920143735,1808021577,3984791360,3003958795,2957845665,2855309944,2802811442,2628754300,2615068322,2612304497,2608995031,2543616592,2486607154,2468890162,2465419980,2417545544,1581900092,2611404737,3155609395,7298906984,3306001055,3013137593,2933656784,2727126837,2472379220,2454550385,2434652152,2413513833,2350069570,2069282135,3634541841,3131862665,2435574373,2738362041,1670237720,5076164250,3700665152,3335400834,3032384384,2808480947,2785838722,2759537994,2730906013,2579898822,2579581762,2532396442,2391232013,2051178407,1845809194,1789933433,2834679487,2467065940,2386362855,2489956787,1980434025,3785922632,2872523304,2481660365,2760436521,2438231690,3029894663,5210059734,5151899954,5117106561,5051041587,3991980193,2997208922,2878072982,2819405894,2799355845,2782723851,2696453910,2613365113,2596072432,2563386032,2545397410,2540606547,2478733674,2445536192,2437742084,2386558061,2383062575,2342236610,2325771660,2283872093,2266761291,2047407790,1994463273,1991226303,1923774815,1825681842,2451869440,2437432107,2419447245,2413509250,2389061462,2388935452,2338594332,2322717285,1909962047,2645837107,2526219251,2475499602,3770220293,3101606397,2807570770,5758503909,5751686107,3519638873,2009760773,1272514050,1771545810,3294528785,3001909821,2962421687,2883504732,2812847421,2378061507,1961508262,1942637060,1930854617,1926101557,1804058937,1642265697,2436320783,2405528420,2526599767,2406806591,2412694720,2368738903,2722947463,3662716203,3558928697,3173946220,3160980797,3009465154,2956635662,2884412724,2851916175,2843986375,2706736120,2696826085,2687898594,2648905265,2643060532,2630619077,2613537190,2579628191,2567646557,2500168140,2486322744,2425877164,1931640351,2020425767,1791226124,2378086052,2165149193,2111702093,1908320591,2099045354,1951571897,1883788793,2135740991,2264963312,1983473880,2140645857,1988313555,2487644694,2350872487,2331625777,2311360432,2249153474,2120392604,2030045711,1963530902,1957400205,1953092457,1944356793,1936034062,1925100722,1920782482,1830203963,1826215462,1782945382,1781492597,1769665192,1756355437,1835696945,1784658940,1996149121,2019373730,2348867555,2302426121,2325006115,2186224572,2157177582,2043827722,2042067115,2002563515,1914342302,1882891771,1892967633,1839274184,1913906971,2408605493,2390824082,2388540011,2364550800,2304520785,2302997037,2262632365,2168022810,2120803674,2114620592,2045026753,2015186563,1922961071,1874474992,1863362883,1825151213,1775729762,1725120013,1695837052,1961517291,2284042960,2334988077,2498040872,2321800463,2319319475,1723368132,2050486612,1733879635,1740070623,1693035895,2297495792,2273457694,2231191720,2212783942,2185172380,2062371421,2041780392,2023595027,1995371013,1984852905,1959035780,1935097072,1929129655,1914082321,1787521503,1785882203,1726939147,1724726867,1697044397,1772130797,1681521511,1650745602,2337874955,2429500650,2411613164,2345072630,2332948424,2273406244,2056839792,2048587734,1934610065,1933175665,1909376680,1878290843,1835523680,1828858154,1761577164,1758898783,1731767225,1961656291,1824998582,1881907635,1778172722,1849552614,2261411270,2128619012,1846193214,2270926147,2256964680,2198956394,2168691982,2141876655,2140747163,2070650177,2053664642,]

count = 0
for uid in uids:
    crawl_person_infos(uid)
    count += 1
    crawler.info("count:" + str(count))
    time.sleep(1)