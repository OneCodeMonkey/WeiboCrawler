import sys
import os
import time
o_path = os.getcwd() # 返回当前工作目录
sys.path.append(o_path) # 添加自己指定的搜索路径

from logger import crawler
from tasks.user import crawl_person_infos

uids = [1727870872,1700862541,1725966687,1728063222,2242188273,1970176620,1930485297,1897727643,1874609342,1863009035,1725914072,1797701177,1723037922,1722106655,1726761334,2147227365,1783752760,1887680575,1968130533,1844775624,1725876215,1726375072,2198267105,1868913861,2281920213,2194795330,2168914923,2157858030,2075934631,2063491881,1971268267,1971128367,1933816210,1917865413,1908898261,1907672117,1890555205,1879618067,1850075313,1840394053,1825849607,1799732031,1776550024,1764106883,1709119663,1589629271,1589610570,1440463315,2205845365,1985331515,1778406640,1777398310,1347070033,2208390611,1723747032,2126956633,1621152525,1912942250,1776575882,2023589655,1778244742,1921491363,1902269841,1776047243,2685567601,2608495071,2566107613,2457743427,2420795737,2392833925,2267183495,2237033741,2196648925,2109450931,2108758963,2102785765,2099340660,2095862142,2025528463,2022792737,2022321115,2006861823,1996098125,1976782225,1972553081,1967497171,1960379451,1953063257,1930034147,1898211422,1852057380,1804740132,1778380600,1777724750,1758723925,1728097840,1699000664,1352577434,2407834572,2061896681,2128871081,2316998865,1357966462,5394767053,3525551007,3231917594,2906058047,2814281044,2609615047,2460126852,2281214885,2183447821,1986723747,1978026141,1962364233,1961492805,1952970823,1777278980,1773532552,1747965000,1639173160,1623194935,1347511717,1588575902,1583800907,2076501163,1789473925,1440467711,2134021883,2309480323,2300794077,2264081237,2231545254,2230131861,2217259037,2214195100,2070912065,2022040591,1954427717,1939233805,1930301564,1902654702,1892808754,1845912321,1845755617,1838928380,1824634003,1778341151,1778145514,1741613215,1661824463,1650947905,1776771995,2590628321,2718874492,1778305831,2467133120,1785074174,1971970851,1347513350,2216034795,1803856645,1896584400,1777182044,1923473773,1716610064,3290413017,2429267231,2400404685,2370918471,1359048434,1356251835,1589491885,2050030772,2287383405,2479694185,1778240354,1822591172,1778300155,5037858027,5123397125,5071202868,3987396134,3878024113,3563054283,3554801803,3514173821,3254857194,2846543755,2742864123,2313887625,2236404694,2158027541,2044440971,1984619923,1975025543,1956943082,1949504351,1946465393,1908911641,1889323621,1862037871,1846179405,1845339563,1778171650,1768670293,1747553473,1704524531,1685919033,1661844675,1355365083,1318523127,1728115905,2205317317,2190449977,2021398397,1971634237,1960010161,1833961503,1827447545,1804052681,1773612272,1765453787,2316460807,1355502315,1869565811,1966420547,1723129337,1927091781,1778343815,2133420773,1885020723,1588370805,1936368657,2260784453,1778099544,1864762777,3065187507,2632175853,2617599753,2583146387,2475954882,2458609980,2453517255,2423032050,2397470011,2327471357,2318371814,2291074290,2286619083,2279619192,2265561157,2252092963,2156472505,2153193607,2104635641,2036882613,2007380205,1998029565,1988901925,1981166667,1974919141,1944421483,1907498137,1885669901,1856834454,1924589661,1836525743,1824136297,1791972803,1788747023,1778822055,1775866694,1753091841,1725984885,1715158273,1710095670,1589738165,1589621074,1709692271,2516466283,2284706205,1889780155,2401746495,2295673885,2232218082,2173463121,2166100557,2352938851,1911688561,1993677105,2891264705,2208278661,1784139180,2317539421,2313525253,2310391961,2310216703,2291604285,2279437625,2270654395,2248405501,2230118481,2133421027,2095042761,2087809905,2079268213,2075376291,1981566857,1978785037,1934821877,1923663275,1917135580,1909471221,1906593091,1887858831,1886587420,1858299804,1856122865,1845205075,1843743105,1835913567,1835715865,1820731453,1818402293,1817091004,1811394404,1809933943,1784030692,1779447781,3391724852,3173037827,2758947511,2641749635,2517872603,2443329043,3013824731,2350703787,2391997631,2861148824,2337088701,2806732667,3764121801,1923255147,2913495533,1835996624,3907667872,5380202803,2496149373,2908702375,5243012489,2480364581,2395644001,2336963812,3916754070,5617735722,2340705434,2485817163,2507914243,2397041511,3954347987,2951046261,2653973831,2612015151,1757870057,5672670811,5189377184,5543105493,2518190341,2734766011,2714596853,3065478472,5320936105,3946180559,1951945777,2436931043,3152998694,1731879052,3152813185,3040618493,2713224535,2693499633,2660019404,2497957134,2461843457,2419015805,2354241925,2324977595,2392445713,2566461734,6222953197,5096584985,3950120548,3229116567,2875736012,2403828003,2614320935,1577185132,2412875281,3226684297,2600701405,3228283163,3144167572,3824430915,1960397407,3190868262,5933348412,2702357997,2713382392,2810988267,2382214835,2881451560,2879465520,2478298295,2921088405,6027105740,2521248001,1793420801,1630173885,2703712852,5031790350,5369946410,3979133315,3548781611,2697163983,2393283625,3830139535,2920114373,2607438745,2740302403,2342465585,3863666324,5158224114,5060126171,3869685633,2040569365,2518214970,2728795984,3478498773,2704490515,2403976733,2447693627,2733408791,5022761660,3851325440,2651376077,2609912202,2593392604,2516915413,2484007183,1955113373,5289213784,2824841152,2472819423,2669989085,2909341124,2552451851,2394320565,2367825413,2166306281,2384164043,2919896524,2604854403,2448473760,5547227671,3881504531,2708669421,2671270763,2609029115,2586986332,2463204931,2365108432,2410450277,2376605617,2715533980,2471885493,3950116424,3917861965,3898873173,3861236847,2756166813,2750336521,2705235361,2687153825,2628903060,2611309867,2463305421,2458004615,2452604590,2421613797,2413743953,2377225703,2356454901,2283675364,2628461251,2389617811,1795476123,2334119025,3122459201,2692509297,2633830693,2625355335,1904537911,1774094334,1576856435,1794023537,2422765022,2403709367,2011316535,2543069752,3181313811,2910184427,2821901681,2738621304,2686580163,2565676047,2520978343,2519962137,1785238015,2979878867,2723923852,2009783763,5019720727,2397471760,2451501957,2356079045,2354316427,2574912317,5104497388,2596477837,2540536402,2502929865,2472952261,2411025720,2327007271,1342967873,2494008847,2407519821,2734418275,3912250901,2809283547,2782203415,2554329977,2459879843,2449739050,2368041142,2069169965,2662101887,3215279054,2396322064,2327543584,2709114725,2492230532,2431579351,2881143771,3612812232,3237306814,2839542420,2798277250,2794295893,2739482732,2360540857,2352465173,2329821890,2327435325,2319876014,2319220107,1803503125,2311497717,2533493047,2495012373,2439762832,2386506613,2394580964,2696454910,2704644231,5085016366,2546294020,6499418646,3315607805,3225471453,3157068764,3101565235,2998038543,2813831294,2751887803,2695637373,2677912413,2647290094,2639315663,2637386241,2609637533,2608242503,2455386947,2436498824,2430981044,2417142752,2413726503,2364756044,2332797463,2318481691,2724647364,2689594577,2950231357,3859004331,2820083523,2606559397,2450376862,2449223165,2407408851,2956858845,2564607965,2675489411,2546959892,2398083537,2332370180,5643411575,2422719701,2727731005,2513360337,2536432103,2499629625,5476039673,5380036526,5031852963,3280953050,3259451334,3017515623,2618424227,2518356765,2480254000,2459288564,2453321564,2443047337,2437236774,2383558964,2370393122,2332105863,2327990824,2073575170,2011019061,1970293277,1805297293,2382596443,2883346402,2503351624,5102863852,2835763701,1947535354,2577983553,2598810203,2380625103,5796903283,5345613186,2627571200,2606483231,3211087580,2512670940,3863888015,2426738063,2582569364,3182772020,2857308352,5643260251,5075929660,2656607103,2438678154,2248096651,5515168660,3192709597,3071495503,3752843150,5097363487,3764730193,2216914142,5643863224,2879718780,2631515393,6235621121,5941125003,3480091350,2703860754,2692630831,2232017357,2400662535,2691516587,2612497122,2396431173,2313675871,2090037063,5118190880,6039262866,5847631341,5043109827,3264623051,3123130301,2758051303,2678159860,2675765124,2295398732,2291785983,1901639135,3104684280,2902245965,2874963445,2708081600,2680767233,2677029744,2661400424,2646640567,2584295691,2561012587,2501845900,2371472792,2104733003,1824601414,1767160015,1594549233,1275111644,5434833492,3640409684,2927565682,2841477070,3296071831,3178161042,2657204581,2673894741,2405409391,5271312876,2452388465,2412399514,1767872950,1927761813,3050898402,2300716117,2268788574,2671602490,2408821381,2771060982,2696398791,3348161864,3254384707,2811917604,2790182465,2641897471,2585854520,2478832872,1976347435,1965340477,1810654112,1794583167,2964253872,3612070225,2863702422,2877206122,5523501945,5460787045,5098131027,3733979817,2834371292,2685674690,3743162457,3291261722,3227044122,2943329684,2935948235,2911384087,2881804952,2742319745,2727197642,2660046681,2606758425,2606248550,2440298154,2318020273,2096829290,1905450431,2647117753,1874077667,2927581307,2961754240,2657528291,2469879464,1244438031,3173002187,5824726424,5462529229,2445008597,2875880237,3186873277,3042792292,2877598740,2840271235,2804750301,2530883945,2438921510,2278824084,2170902313,2884307820,1633844564,3863542274,3185349162,2865883544,2801539771,2672579402,2448068912,2283274575,2267116144,2716306673,3027856883,5072196172,2956170144,2303245305,2234982917,2112542924,1965074007,1850738552,2643595697,2414402165,1963786063,2495522572,2242459362,1966934615,2388358804,1971383907,1994567234,2311756060,2001541750,2590240840,2482314347,2465456735,2421786852,2419352544,2301913553,2259313887,2132688517,2094368902,1921707083,1910800240,1830320435,1777681674,3831113677,2105823925,1912648164,1746497354,2299077212,2248783747,2298139640,1954062945,2334463462,3171115774,2433605073,2244345353,2702761904,1950286602,2295335560,2346590431,2119605223,2900644541,1806989811,2300304667,2315484864,2383856804,2462284324,2596906174,2352491010,2322056144,5675280615,1998835585,5058041090,1766021733,1890682284,2905047450,2351297484,1860840392,1763023712,1756319251,1968112065,1927119735,3234244450,2068574457,2610922735,2429962914,1829326650,1966480233,5651067690,3313787997,3306585915,2233847230,2155407923,2043579611,2022329073,1942574355,1941850004,1940630727,1880718822,1870236422,1854195474,1842468520,1813158037,1782815957,1804298462,2443421163,2355284822,2233235802,2180976363,2096170637,2047572904,2038370205,1978760981,1945249161,1837876362,1800396054,1781010815,1779194714,1237772774,2258297260,2891441533,1955106143,1976127582,2339378343,2130485572,2254537064,1903047435,2271047312,2011885057,1770969033,2726054921,1970879565,1627597323,3911291743,2952845234,3029448925,3038566087,2063144021,3208669287,1791960990,5209796354,2308433820,2335043540,2485892251,1898733895,2158672914,2812352823,1815093831,3272364230,1749057470,5601886312,2302241395,2936367681,2470996452,2449174764,2406292430,2304924430,2277358383,2243733750,1980267351,1949696025,1831157511,6070606503,3987216923,3958372170,2420764695,3454595330,2881190252,1865200280,2308198154,1870303702,2828770702,2399640222,3147432761,2608320697,2657662462,1650546142,5113598852,2292072754,5500674659,6872856943,6323503719,3816426740,2064117607,2769390097,2165676555,1785240557,2027332113,1750600990,2869358532,2243653154,1925399060,5026554136,2863624032,1837967084,1893070422,1776228191,2299734304,3919027007,1994356717,1924470142,2256008790,2014178885,1907424081,2359703853,2342162400,2255078220,1784893312,1780494914,2409395785,2396258421,2372151613,2323311740,2318064591,2291205051,2243442920,2069921290,2056906692,1988532055,1975014367,1957774445,1953016915,1903169507,1872938740,1868449394,1820312031,1788995371,1780387411,1774212871,1768235773,1761938074,1761657260,1839379770,1862513250,2183099293,3047846634,2908180657,2868973950,2843082967,2823184413,2815746811,2802740524,2794412840,2763474517,2755772134,2728496267,2698759420,2652510082,2623146717,2605759122,2586674997,2508261061,2504720992,2503584222,2456490883,2403320235,2339085120,2326191794,2305473450,2297305492,2294245965,2240103270,2186790981,2168820244,2126534502,1976113365,1833397627,2794425400,1856865724,1781326170,2314226810,5245383993,2770370655,2394278571,2389721242,2350065542,2302041200,2300462192,2288552974,2283486764,2276350272,2264407084,2256457105,2235962820,2156895047,2631800432,5560639110,5519586697,5315756276,3876469593,3547295753,3269795401,3177519852,3149536240,3050013487,2479904392,2804633840,3034365067,2736143303,2545892747,2927663300,2422375847,2342978873,2573693940,3493066932,5613187925,2048861847,3205129520,5266648436,3452868020,2473558627,2822010907,2734962943,2234498305,3270747425,3311981705,2440603461,2471303702,3291912001,5368181127,3142406445,2843486840,2717550353,2504529667,2726610627,2842409134,2617819220,2468372662,2496150067,3478128727,2675786501,2880455660,3991543128,3784296120,2921631300,2457815965,5043356062,5501811791,5251563056,3176072414,3014484197,2679291503,2800443464,2799630220,2794262104,2788585292,2704228515,2571930460,2451942821,2310840314,5069098563,2462865780,2863786640,3071691863,2993866502,3795117937,1831443185,5206638845,3485524643,2484952397,2468648672,1789520713,2467688790,2454343794,2772728721,3021768841,2738616482,5312787256,3165447120,2838481867,3942917406,3729889182,3227971325,3221461180,3167397054,3153916444,2955626904,2912139145,2838351140,2787360380,2690658183,2675659544,2658106741,2485392541,2438897324,2313750410,2243591047,1924417142,1646109522,2736478652,2437828452,2241740322,6448355371,2196891941,1979848583,2294708724,1977320660,2889678342,2113441613,1891435900,2534574604,1854996835,1908190513,2281502700,2277141562,2030095847,1761806110,1901877880,1687890931,2945291992,2331503107,3091761794,2314838265,2414378462,2194085083,1853769582,2089196705,1904414005,1844312072,1840630991,1820882462,1811408582,1820409222,6009018196,2674679403,1959455623,5403473616,5038746991,3863460551,2990984533,2698382005,2679540562,2361526340,2295095800,2294336587,2159449602,2077239925,2030122201,2319082903,1819804787,1995517303,2599731844,2031048321,2010577727,2368866300,1962927800,1784695534,1782963873,2082067305,3134618533,1978786105,2277242963,2291146843,3212146172,2372017504,1966406523,2704920887,2066969805,6167594570,5693892094,2254351510,1856062037,2436740320,2164683071,1934701272,2909236037,2394358551,2393553231,2278441190,3174713584,2322890665,2322325067,2193750432,2758035143,2288616385,1966277207,2812536121,2160366082,2269288482,2014607101,1828138907,1874173141,2266422503,1876080357,2382303924,2033750820,3803946124,3625843534,3592092324,3485298540,3242777804,3223725703,3212968467,3191474782,3169977347,2960594130,2919782722,2885645760,2849029170,2805145201,2682335603,2650390411,2639588743,2631029962,2411233483,2376454821,2335068001,2259659105,2131355545,2115914562,2091612827,2082748783,2053203923,2048622142,2192171732,2307237632,2407659824,2651696623,2402704730,2312863855,2372971361,2873870834,2598741280,5043595257,2485522680,2389923487,3802703708,2786194294,2432442064,2274813870,2681454033,2813125822,2401550125,3541095755,2602101381,2325500172,2196471222,2345881032,2339789737,3294275053,3292386137,5148366482,2536856673,3826077631,2448040880,2421809360,2326611327,2298920353,2293203950,2287742807,2251021630,2231403660,1929930975,1817615127,2336187623,3268295034,3968785046,2165091064,2475706960,2307567672,2163486824,2671974653,2480880192,2191043234,5506526066,2328564582,2328206994,3762327737,2956037484,2253970117,2276564594,2157659303,5281576692,2549287267,2440490160,3981452105,3086328843,2695538381,2655884893,2214809242,2169845910,1779863401,3553136445,2403479897,2048474342,1979458253,2679862014,2895670604,2383149121,2279676920,2295014112,2878137664,2708874497,5586787540,1743057331,2334426400,2186271345,2931431653,]

count = 0
for uid in uids:
    crawl_person_infos(uid)
    count += 1
    crawler.info("count:" + str(count))
    time.sleep(1)