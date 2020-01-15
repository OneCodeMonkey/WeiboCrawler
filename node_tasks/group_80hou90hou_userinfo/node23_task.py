import sys
import os
import time
o_path = os.getcwd() # 返回当前工作目录
sys.path.append(o_path) # 添加自己指定的搜索路径

from logger import crawler
from tasks.user import crawl_person_infos

uids = [1904332351,1779776850,1733665833,2839673454,1688801490,2606561285,1843646401,1787920204,3009012397,2143140811,2471945670,1953345104,2703317082,2767408471,1806339522,1638839624,2468140745,2253106687,2128109940,2023024863,1877824047,1876348793,1860851235,1855176743,2710184820,2602736203,1768574775,1660690887,2393252742,2685872535,2215822921,2164483475,1959220337,1779185237,1945559132,1759245365,1649850511,3151227457,2794908653,1728005650,1723109587,1440476482,2891305795,2878922951,2211614211,1954428344,1819442145,1788840113,1779611511,1674526177,1581681592,1437565584,2878074200,1440455790,1440411343,2117261042,1775844545,1439098262,1439062422,1439001523,1723744412,1440502027,1438666915,1727890530,1440484594,1990043282,1974236100,1752979201,1695221472,1440451225,1440392615,1437560965,1352579360,1349132203,1348148027,1347069711,1785305600,1440470974,2040673897,2339579727,1357966915,1440105027,1440408250,1728053052,1440393994,1440442644,1440469624,1727924944,2712310020,2676893481,2671703793,2258167694,1923812381,1889298967,1831548644,1440457110,1440401511,1437489345,1358989840,1807669387,2869736762,2672597067,1348920180,1440287173,1728107567,1440663223,1440103463,1438687662,2161970722,1440415067,2760662943,2012626557,1840132685,1787558935,1440668211,1440495845,1356228080,1296305127,1440467582,2602525931,1728109990,2030415711,1439043634,1439091782,1440663655,1440494751,1727548101,2872531567,3412165814,2741031142,2687695650,2674103317,2557242423,2356218061,2303080681,1909782665,1576542527,1440491413,1440451371,1440437971,1438912043,1437555805,1437521094,2344357882,1792314450,6347184744,2733052911,2480525941,2209967343,1761496595,1728082885,1440393093,1440476501,1440468371,1923348043,3179881520,3172544581,2512539943,2264522067,2203658104,1784893074,1728099337,1727848573,1727509873,1723021592,1440487780,1440487477,1439636651,1439658073,1440479074,1440481544,1440461265,2365086365,1440400265,1727889060,1728077505,2408007331,2787577170,2415827613,2259493014,1780528807,1438909841,2609989397,2104200722,1720685191,1439100293,1873847035,1440405620,1440462133,2626547683,2447123710,2369988040,1995277527,1923158801,1857844004,1817085674,1728113320,1440284440,1440471245,1728046245,1440484317,1727435541,1440411617,3078329194,3198221430,2955621767,2948212083,2721046711,2706312662,2438825685,2372439524,2268265914,2017755371,1440498013,2354082991,1766703593,1440666461,2485005891,2814991882,1838082201,2872359611,2488313984,2295410150,2257577874,2218753572,1957109101,1948492562,1869664835,1440498893,1440408537,1925489653,2430450652,5600027123,5128632819,3197461440,2674261251,1864173260,5046425334,3751381524,2734726117,2729835173,2424583300,2090911235,1995110681,1946619917,1800730735,2987155357,2845611354,2718439301,2400743352,2302399152,2294816532,1866312342,3179022181,2596884762,3058042307,2632179961,2336960240,1933420460,3341974514,2709670222,2655869927,2627875054,2436458700,2406225960,2296840093,2294146403,2247067192,1840582241,1773579942,2253729012,1743888220,5589132133,3098706715,2661963085,2328481924,2027206997,1762105917,1688445914,2819335100,2651649032,5625589548,2971244300,2604179717,2419090642,1795686654,5298301598,2933080184,2891231604,2695249791,2649299063,2404387440,3863362424,3496522082,2880621174,2708121764,2693220110,2471301435,1864590792,1816118021,1320135667,3204193505,3161024762,2982625787,2396958632,2145403067,2024813857,2862168624,5182399547,3627912512,2696556805,2479373282,2424886304,2297924284,2357387941,1957905571,5620338445,5323711303,2434931722,2404533413,2386709337,2369455360,2345088154,2182594587,1739538295,5235183552,3767432075,3648690575,2704656140,2408665692,2400550747,2395835877,2394572340,2290489440,1857788010,1835989051,1831421663,6217857366,3693633954,5367376269,5019299822,2702970455,2689567893,2654610763,2653573491,2490661417,2356858987,2280237113,2262830483,2532010564,5666424178,5237951135,5213362572,5116324885,3278637720,2612990860,2387627357,2387083882,2331470135,2075505503,2032791442,2017836771,2115968924,2090356967,2005059670,1945871380,1842262267,1765656400,3503337542,2618598781,2355180261,2378651334,2612034305,5287402776,3968591322,3606632211,3391994414,2849369545,2451892587,2376979647,2295227520,2169190710,1948200564,1922488837,5647680274,2813287254,2770560843,2629375031,2563817232,2445576183,2338896285,2237478312,1999385025,6072330848,5376526114,2783160287,2528272351,2411655393,2293512832,2191577402,2175719334,2313796387,2481793601,1987833511,5426635292,3934377545,2891227640,2885808042,2835858381,2394188081,2332743954,2240138594,1950441211,2721039375,2696675821,5832240988,3973341158,2948643462,2948096400,2943934652,2885661804,2728435814,2628076011,2461124002,2448474664,2397131092,2294645610,2250843645,2192653494,1946804762,1917344057,2506655391,2691080185,2267428621,5831387409,5651752202,2961308332,2960746150,2901680412,2886295622,2358803503,2096233613,1763673714,1614127397,2323833255,2847508525,2987464742,1785102072,2922795834,2540902657,1793363525,2951419802,2943561530,2921137900,2898275534,2421440807,2327655955,3192384790,2816215543,2697070891,2447695154,2512814141,2095618164,5232719719,3289090184,3141431362,2964308774,2467595460,2538352125,2299883951,2452841732,2403752957,2340191082,2308183937,2297018300,2160485772,1987878190,1927948462,1921730120,2620669593,2365526842,2642781182,3870813346,2483887584,2469033094,2322322990,1988387587,5336351851,3793264157,3323484360,2933540450,2885963982,2650781865,2461060372,2401310081,2154340377,1916141140,2316325350,2460467960,2342947730,2158285377,2942743705,2997441270,2416001005,2105945321,2285031233,2193472651,2005382095,1989349277,5640706744,5249028677,3986725585,3577669884,3458156964,3040610820,2996789424,2995524824,2994752594,2973476954,2658675562,2634768160,2509947750,2454230735,2845370897,2657122437,2450395905,2449694754,2437825102,2364578044,2358497700,2329201465,2306314130,2305761724,2269640564,2126223134,2032720182,1787505962,1774240245,2987940292,2088937583,2952639891,2376802230,2240601085,1768437005,3186053301,2407489792,2357544915,2350132520,2329638272,3929745970,3225746251,2486303932,2476761740,2386208434,2335747752,1965349937,3277827671,2763100571,2558057743,2007069447,2566908161,2373856501,2317757911,3219060677,2407449314,2359562475,2346354163,2312922320,3829709127,2979460702,2959281930,2916954374,2878701055,2831413283,2631360104,2531572947,2509891264,2252567823,2638319645,2627889652,2475263660,2471157854,2440529351,2391645384,2380022177,2371530382,2363034984,2351862705,2349917534,2342487373,2342383952,2292490980,2089013245,1739250003,1737911845,1728243080,3188659312,2394511453,2373254374,2367199250,2586579603,2493398854,2474830857,2461792743,2425321447,2416874717,2413616085,2371885180,2168750173,3914970648,3196037130,2882825595,2480958034,2437903167,2352445744,2470340320,2352160621,2698320797,2684231680,2366019434,2345948050,2323858780,2323464192,2891221672,2488040904,6642096389,5736154581,6399800975,6690155531,2523217995,6917395046,2489055030,6826911422,6826094021,2336538905,2411587881,2129648747,1831242663,6824212076,6232778024,3171454390,6824270654,3890764422,6235352947,3979425952,3996746619,2602806082,5352784348,5119434622,1623060421,6706301873,3831140183,2309596052,2061914011,2833630415,2882566107,1813198490,6734613464,6036030346,1987216843,2640599867,5872580411,2566426255,1987208127,1917830283,1913732072,6222037628,2196587391,2014939085,1898622457,2388994234,5629485767,3996747687,2438067780,2293112700,2017519987,7021226578,7020793753,6872061362,6871503335,5097698764,2257019787,2018342031,2697460893,2006466921,2901485185,6533401698,1791749927,2391808910,1794954893,1956127357,1962314657,1849414183,6511383690,6052575126,5845718100,5793511459,5176269869,5091874014,2693098911,2475375910,2450394610,2403128101,2012751257,1736588342,2871523914,7022070605,7021821735,7021429171,7021347008,7021284182,2390604284,2568691815,7020952231,6683896004,6502723650,6228985753,5241106719,3787504325,2949596100,2848532324,2824295911,2640776410,2335952450,2090896070,2036866040,2856366380,2887964992,2482981374,2813647532,2357571483,2322809933,1804459193,2078597131,1963266361,1957087737,7021976125,7021409347,7021205988,7021174405,7019262901,6871590302,6246209992,2104948207,1109793567,6052900105,5635514761,5519515927,5162428219,3996473808,3571519125,3193195230,2849049693,2669765031,2445976262,2422855420,2353509522,2020185661,1987508032,2848083971,2565184747,2465439372,2113448573,1792445543,3854365049,2711684672,1996977150,1937528167,1751805943,5456108769,2575106160,2469336244,2393094532,6235405305,3121052760,2964138341,2485278332,1951216907,2611495641,2364716465,1949353821,1835832884,2436894812,2403125354,1947687072,1922261342,5252113202,2339132070,2327996593,2315382374,2093267237,1985532710,7021482489,6872074453,6872063117,6871958286,2384966574,1998792407,3257247332,2581753560,2332156461,6518540235,6233954899,6186688745,5864496855,5620865517,5333147923,5312958496,5042955724,3968030802,3964021423,3891912452,3787187947,3773726774,3709868891,3670655097,6093170405,5200978413,3807209474,3570566471,3362014910,3155756664,2995281320,2972547090,2940500283,2932233572,2891806644,2845231172,2693044663,2661409333,2656071855,2603266424,2511248584,2474697074,2471421600,2460915690,2674300775,2660202631,2427795702,2427794882,2422670952,2389218410,2387654634,2374057384,2366116162,2353900781,2352251702,2343178145,2327970391,2317216605,2294032610,2290432712,2262687041,2249590833,2185432312,2247864085,2201261465,1963682551,1918421082,1863504832,1782307372,2980198323,2434935474,2419502660,2388928540,2365672734,2313900994,2304904280,2278201385,1886799025,1885208702,2119052374,2113920145,1941454342,1796879847,2190406241,2471844892,2180110855,1831066627,1848229437,2798118035,3969270271,3025626282,2019485525,5121959241,2488785964,2349315447,1824184352,1887833497,2410040454,2171714322,2644192241,1949176943,2926592481,2162724881,2171217275,2376346924,5515863863,3885583048,2638323137,2531636407,2065860371,1940422700,2549826173,1804381852,1935499905,1867998605,2660780722,1957633817,2438660302,2717477114,2543975162,1890277132,2710848070,1991291541,5997777032,3157137862,2332210921,2212398433,2446967180,2523092487,2316421380,1840602994,1922985007,5904219178,3187146383,2702755210,2641401963,2625670311,2305700464,2243695535,1987113917,3694710932,1922809242,3547400097,2259202743,1921463145,3165371432,2412265373,2069724674,2133311553,2436784302,1774064451,1708096481,2689003913,2393319277,1811444380,2447191817,2406835581,3730032214,2723478521,2516623865,2395055171,3509498362,2944292377,2724478190,2612247920,2487543527,2473031367,1798542934,1836312811,1783407210,2405449193,2196495353,1773568485,1561376200,2846939440,2396938962,3039035167,2494946597,2417189157,5631349545,5474237443,1869668627,1868053087,2011164512,3654561901,2324062003,2515911345,2261257360,2367228355,6284674060,5233295094,3947530848,3878237214,3800181650,3774281614,3686912192,3486184797,3128910800,3012357275,2973955015,2876478230,2290906931,2259269935,2168650837,1804064207,2514047460,2481508600,2447982645,2447681187,2406518041,1783385521,5548736719,2495170141,6341841918,2313839702,2520076855,2363180077,2734481573,2736588754,5482912434,5270960427,5128863541,5125855060,5106093111,5035884703,3867268663,3348356344,1950825923,7299047608,6227587620,6001334544,5590163240,5283850718,3987582884,3889025820,3848529067,3665359692,3264906811,3180555740,2959272282,2935787853,2890124324,2876192772,2874191212,2801523433,2716189195,2205819227,2200644897,2013820412,2002622765,1976511740,1919909594,1809006222,1801294387,1768795360,1751750001,1747542970,1776506972,2925159963,2892281743,2418734092,2355814535,2349613745,2305263942,2277350823,2250047037,2194659245,2182506260,2164318717,2163596381,2161296733,2156298915,2054463943,2040746084,1950909953,1941954487,1911091911,1908918443,1887827784,1860435834,1836149400,1827421300,1773771743,1772614880,1727985001,1715190707,1599038514,1572667832,1845273703,1741849705,2314461997,2301895491,2270148787,2142271244,1976504765,1771589780,1725495094,1728129674,1837476855,1785029901,2306497031,2196386837,2022217741,1976874253,1975114731,5417684099,5308131147,1794368795,1766735473,1778205774,2210066301,2168478653,2147853292,2083578705,2081227131,1934699042,1881794607,1838064983,1785832827,1778425600,1776549584,1775975155,2244334917,2467140734,2381302861,2366004792,2344059575,2343108775,2341209555,2334218803,2325153473,2297282005,2295432813,2212141233,2205597314,2192019345,2188938123,2184324314,2162453913,2128415872,2127255252,2116975087,2053653691,1825504385,1785847027,1761245291,1760774137,2340758957,1980359327,1884504824,1727015703,1774916404,2019659521,1749890903,2257700715,1811125911,2339239534,2320874331,2316653115,2301565785,2405505077,2583937421,2110200473,2295454753,2680763711,2313950645,3488926645,3656731553,2681766951,2261566701,2173343905,2381628477,2315803665,2090980387,2323465711,2399140704,1923053805,2296946020,1912676204,1800404712,5017546795,5833541428,5020406630,2717524764,2645515044,2480748283,2405696925,2316167103,2290942620,2243839341,1566974043,2287105220,2262503477,2354879703,2454454617,2347213733,2268540975,3740036330,2950929860,2578755221,2415090345,2410982625,2366100657,2340238861,2281595345,2286629064,2215563581,2403547221,3393664260,3228071163,2255178673,2393866714,2589546701,2567124147,2497340941,2343676785,2265570477,2238593752,1569496860,3236598915,3124632517,2761473243,2726122335,2657129293,2637283842,2438071437,2434923241,2406178435,2387189545,2343549424,2230347193,2199729211,2355424631,2439756107,1788743011,2380499523,1629964850,2816628604,2601487547,2002313271,2458421622,2644390703,1581220922,2311989807,2793390532,2351742180,1855173673,1853251345,1216210317,1843842713,6064763494,6016920462,3419074442,3219865164,2832512205,2816709123,2241271571,2614330705,3229616703,2393844604,2063410697,2397543002,2316611365,3214196797,5285365828,5023080712,3914386788,3071821620,2783137067,2469717512,2349520391,2120204961,1757491745,2683505730,1800190465,1805776394,2136595275,1811971681,2263680194,2449637615,1726540961,1887133654,2166301634,2379695057,1884884847,1946874034,1922582185,1786890865,2105362277,1820509680,2155643342,1975053337,1964220353,1896905567,2046850341,2041793737,2023812945,1978741241,1970693687,1968519517,1932762917,1858798673,1763097880,1930988487,2533064812,1831765897,1784157435,1784293237,1775967103,2116686030,1910239125,2452494133,2453317911,2385806753,2349644195,2340837077,2308588743,2403595114,2476919587,1798801785,1710822907,1968340601,2231956545,2230718021,1849997873,1977920695,1922811335,1800834927,2115617837,1773165650,1931692340,1925169737,1894508950,1862970320,1850952597,1836185524,1833452222,1833025932,1809931585,1805189641,1785419510,1779211187,1763695935,1746687305,1905491003,2384490492,1733684373,2119513657,1924803761,1830612190,2214306991,1954015891,1728675513,2257194413,1791173434,2404585853,2316605545,2301984741,2169956391,1969247265,1855445757,1758328881,1897507473,2063578621,1774310807,1900756675,2115468312,1959359951,1842258861,2089046513,1899989665,1812038863,2127310915,2028214221,1751202787,1970712603,1910778827,1762429661,2368523273,2359454175,2346101610,2219379453,2130636741,2069898677,2002278754,1943463337,1942407953,1884359177,1882771363,1869690983,1865161701,1789247757,1748673314,1677348861,1693465474,1646991673,1773413820,1978237507,2143395833,2206627890,1881065682,2025977765,1792535657,]

count = 0
for uid in uids:
    crawl_person_infos(uid)
    count += 1
    crawler.info("count:" + str(count))
    time.sleep(1)