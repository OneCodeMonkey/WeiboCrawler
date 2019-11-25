from tasks.user import crawl_person_infos
from tasks.home import crawl_weibo_datas
import time

# 混合
uids = [2146958300,2216162085,1733118395,2535059393,2216161051,3153316723,1734998053,2208520884,2106758822,1721226473,2231419060,2286602452,2146958300,2216162085,1733118395,2535059393,2216161051,3153316723,1734998053,1579046115,3175031813,2272979875,1812060454,2123610381,1797630160,1678185895,2654641464,5936732412,1736449892,1646283081,2652134221,1656186601,5368912439,1651018084,2149032020,1948513465,1837510197,3400651762,6104350592,6042981140,6042815224,5856039513,5360108252,1791936310,2259732055,1661427547,2101446454,2199318164,2114231550,1691771750,1802498701,1849921530,1949918600,1951415962,2083422187,2089180423,2104083860,1946962144,1952781254,2089159387,2071706657,2083937533,2095659234,1952017442,2076151043,2063945571,2077660973,2091466623,2087394164,1948757762,2062950413,1949083572,1948748630,1952206654,2089977300,2843303123,7225902377,2784947612,2672671263,2553828854,2466036323,3503371132,2285519870,1898464622,2151481472,2113536494,5900150694,1938540274,5324654555,6138073107,2779319344,3077549372,2157126010,2197221850,6020810200,2694257443,1855036253,1830023831,2774475852,2057469713,2482639974,2403823694,2541806122,2088777331,2014535043,2722085370,2095870381,2730491173,2401769145,2129725773,2616150523,3816195626,2205016987,2626916710,1862089890,2243443922,2607086491,3207001765,2184174480,2104636892,2301940157,2301940157,2838237887,3826296819,2144961387,2266409110,2257198183,1951568230,1978491497,1844114134,2979730497,2323471092,6276230977,3196237540,3981253260,2767279891,2237749290,1760585257,2610154862,2610154862,1511895392,1897836362,2142775431,2411303860,2030745027,3788128010,1649165812,1973613891,1971005930,1904039074,2504004225,2772993953,2473113522,2005028377,3230530374,2881519002,1948120457,6927453900,5181720960,2804341354,2634435781,3925022989,2187103453,5348222243,2661737451,3242080174,6507926755,2103211991,2140699987,2257204630,5657670371,2880568631,2027667287,1978676391,2803656894,5056179653,2722530503,2330447327,1912583527,2330447327,1912583527,2012572035,2373360412,2084336801,5301781706,2805337060,5907254050,3211696412,5172039488,2492366285,2530781954,2154665042,1860343432,3553076145,1810339704,3996453064,1721019463,2467571084,5263970352,3201397104,1844970411,2803701220,6432711826,2804009250,2082950923,2432196503,2804647702,5529253392,2804690390,1813968040,3149270260,2804650170,2114776732,2805405982,2804727284,2803692592,1870254875,2774543114,1985431117,1985431117,2313735363,3177671122,5261333780,2230239133,2506969932,2804730580,2804699800,6551756563,5784538440,5682293993,2735164931,5303211023,6827024035,2143770192,5582621284,1810545161,2294347565,3163379450,2804693652,1557978402,1810939610,2321077144,3151695131,2111901173,2784732682,2231655225,1948143623,2128547217,2149032020,1844317424,1805434334,2958931044,2007950801,2174632880,2952030073,1867454004,1882162593,1928263121,2389592250,1950889993,1904555433,1863828593,5678869487,2643200511,3017898835,3572840551,2798098252,2589001124,2067020203,1933560930,2184353660,1997715114,2157363451,3748197915,1787354710,3748197915,3731392964,2819505290,5350806472,2830038333,2368833444,2819507010,2695086133,2308940515,1992102463,2163163383,1695471755,5412254261,3359680910,3927088443,1797221400,2945876077,2682980737,2036441552,1904586641,1845939147,2766169885,2374948610,1919469690,1844229432,1904317391,3840675292,6357256585,3316487700,2819484384,2819455830,2559821923,2280729915,2127226743,2120084722,2110317313,1970747324,1874636461,1874636461,1856895440,5247235502,1925248907,1841107961,2984880705,2725871593,1961475580,2011590832,2319725955,5769281942,2881792042,2828527401,6235248808,2874832752,2257853923,1998717245,1914221891,1901614512,2819464550,2451990884,2727337567,1797243934,2110843084,2622145284,2216584617,2072872903,2647570140,2089315361,3260000225,2846099415,2337849815,1996667571,1995160625,1859755274,1855709832,1819878637,1779931710,1894081742,2487133605,1862398754,3169492653,2032115444,2052290760,1895739980,2568534284,2607011297,1876252504,3051196031,2006736827,2953471184,2090514851,2035981147,2015272543,2010713292,1910021900,1871609592,1862748597,1861184872,1828537260,1807661937,1801642630,1777382277,1751224205,1150846414,1966548737,3150664520,1872835594,3900579115,3202655181,5854396270,3638024707,1868540742,2219773541,2107358134,1866913163,1813957433,1868059887,3940888684,6034512332,3314148972,2209086420,2053110955,2035438490,1926073742,1914137323,1861289900,1855020454,1801613592,3329912082,2473913014,1955139803,1831073325,2104880740,2734003965,1898964671,5225956407,1849123172,2006191603,2181217974,5625416906,1865844414,2683041014,3468379652,2781996900,2760150154,2173122470,1977109263,1895511844,1882880180,1878997240,1868235622,1878997240,1868235622,1867689383,1822005901,1806072487,2174070497,1851298765,1873972970,1875570165,1888726081,3190459085,1817050142,3897596884,1998848037,1948080183,1950318615,1876504285,2170890803,1886690100,1895549247,3085132903,2566130230,2517369407,2284244347,2256397630,2125065880,2092913791,2010224173,2008673231,1896741393,1890123494,1868134331,1845840113,1824264347,1823498477,3066147265,1907787871,1935508894,2390625982,1830391800,1935508894,2390625982,1830391800,2127380175,1809248877,2172370675,1851999983,2646275233,1829140880,1883676923,2306376875,3319222742,3308928675,1879629540,1837649684,1897766694,1868702727,1819719840,3926720321,2630811242,2450612601,2310357862,2305725642,2280593755,2259710065,2240516102,2129743395,1952729831,1928838022,1873347354,1866165714,1859529127,1850669805,1848003500,1819882553,1798096837,1764243007,2492637812,1746838064,1742547437,1735217877,1732910753,1730954063,1730514097,1721468563,1703727202,1460742067,1150846414,1056446121,1966548737,1744822603,3150664520,1872835594,3900579115,1704666381,3202655181,1656341352,5854396270,3638024707,1868540742,1749825572,1727154984,1615037071,2219773541,1096952870,2107358134,1865005875,1866913163,1813957433,1868059887,1761743001,1740294111,3940888684,6034512332,3314148972,2209086420,2053110955,2035438490,1926073742,1914137323,1861289900,1855020454,1795153485,1772784484,1759301535,1750477362,1744332037,1742291393,1725678231,1691372474,1674054480,1560335110,1405785655,1367232101,1243515741,1801613592,1667652702,1268226757,1031349051,3329912082,1694516224,2473913014,1955139803,1831073325,2104880740,1889443381,2734003965,1898964671,5225956407,1749644650,1746990525,1849123172,2006191603,1749896482,1533968111,2181217974,5625416906,1767061990,1700574330,1738561024,1571075342,1865844414,2683041014,3468379652,2781996900,2760150154,2173122470,1977109263,1895511844,1882880180,1878997240,1868235622,1867689383,1822005901,1812577067,1806072487,1765947111,1750296972,1750260782,1750113730,1741287641,1717557890,1611754727,1608625763,1605225401,1402232087,1309956235,2174070497,1851298765,1745556511,1738032033,1873972970,1407635343,1875570165,1428862771,1888726081,3190459085,1817050142,1720609370,3897596884,1998848037,1948080183,1950318615,1876504285,1765478852,2170890803,1886690100,1739373057,1799555734,1895549247,2163390672,1151153861,3216739611,3085132903,2566130230,2517369407,2284244347,2256397630,2125065880,2092913791,2010224173,2008673231,1896741393,1890123494,1868134331,1845840113,1824264347,1764238633,1759494975,1738229043,1733773640,1729651102,1729480593,1727097261,1708205615,1705725381,1465577070,1428960415,1287361767,1165035361,1823498477,1687435503,3066147265,1907787871,1722949055,1935508894,2390625982,1830391800,2127380175,1645757015,1260393302,1721450941,1809248877,2172370675,1851999983,1772213110,2646275233,1751625042,1829140880,1760668890,1429292850,1883676923,2306376875,3319222742,3308928675,1660862232,1879629540,1837649684,1779087821,1897766694,1868702727,1787130657,1737375280,1819719840,1635839644,1655434835,3926720321,2630811242,2450612601,2310357862,2305725642,2280593755,2259710065,2129743395,1952729831,1928838022,1873347354,1866165714,1859529127,1850669805,1848003500,1819882553,1798096837,1764243007,1759827233,1745033922,1698488025,1662235942,1658078133,1656675871,1498316097,1496413140,1411172254,1411172254,1286623092,1268134660,1225731954,2492637812,1738836273,1780725300,1738292954,2337437063,1769364990,1839123287,2407281921,1798060393,1772935514,2174424934,2275665734,2035149722,1917972014,1749746180,1706716495,1683252383,1760352442,1881958590,1403176755,1744645592,2345474802,1377367333,1847369751,1930826537,1850906920,1893699782,2607210115,1832049320,2047891845,1751601524,1770080811,1770080811,1738954595,1894337233,5961037163,3745634264,3179920101,2360105763,2314913453,2300784562,2289145157,2249110144,2151855720,2109416445,2108429087,2103509847,2037400663,2035028984,2015790407,1960603777,1936917723,1930016857,1900216205,1892014165,1884612725,1878136397,1852792480,1835758757,1827416702,1820710417,1805364502,1787722230,1778549442,1774837225,1751774114,1751141720,1739934497,1739934497,1737521694,1735463327,1728248902,1709772961,1666644080,1625577910,1411169700,1321947731,1269021062,1246987937,1246247292,1230512590,1186603010,1738027684,1667978627,2374637301,1920004093,1791823805,1188770507,1036390345,1707881817,1671670521,1130469835,1797679480,2256902032,1421407172,3459021044,1864005047,2282279614,1899384693,1743630612,2480204245,1859479794,1910682084,1944191377,1723411315,1711524217,1887880322,1760884727,1937482444,1644425794,1879073262,1688393331,1776785053,1740121174,1705473793,1916221983,3159923683,2890778694,2813355147,2704482191,2653220092,2380967492,2347664793,2338218477,2280681212,2280681212,2211715933,2147675694,2093525860,1973678545,1964593287,1957512241,1929834444,1911070015,1899153025,1888299135,1884705570,1861867844,1851292234,1830301212,1828871202,1827590123,1806718931,1769757200,1769453331,1761673624,1749168632,1748960147,1734531711,1725133984,1699494057,1687385141,1682474973,1682020124,1603245124,1419408812,1401747877,1313225400,1156234680,1119406575,1082565897,1061529421,1660202220,1723165595,1817165950,1703682144,1870801413,2656797614,1736285227,2094414031,1939724462,1931660705,1810362307,1809139040,1743290740,1285743094,1662297257,2489729065,2139494774,1661427094,2005617281,1935440301,1935440301,1756749605,1775488197,1723167085,1765463557,2260131483,1833515901,2181549370,1974561951,1847329713,2193088410,1724151631,5883086016,5873650161,2961952621,2683946593,2503703655,2441519261,2347143531,2196746814,2111441170,2083878515,2071850777,1880343813,1862801757,1855177121,1853979772,1843425620,1827034383,1821534193,1818971485,1809663122,1807387470,1805064975,1804176844,1800247774,1799267411,1799267411,1791101401,1776974035,1757657357,1748144172,1732160864,1729631713,1727211383,1713207250,1691170020,1685964684,1663897361,1413274721,1260563255,1241443384,2856417722,1802767937,1777019462,1777079624,2805209852,2108745875,1820828573,2058557890,1771555473,2070856633,1869714754,1747753034,1811339835,1802877571,1661883203,1923970340,1664919912,1413312420,2160470250,1764158801,1747496640,3101098645,1878215157,2302630034,1289770675,5751292044,2098393000,1768000552,3926428816,1648477500,1849720980,6442336541,1232750075,6266759013,]

for uid in uids:
    crawl_weibo_datas(uid)
    time.sleep(11)


