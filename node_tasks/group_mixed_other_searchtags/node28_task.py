from tasks.user import crawl_person_infos
from tasks.home import crawl_weibo_datas
import time

# 混合
uids = [1867821453,1865001014,1838667950,1415118913,1361741047,1271666612,1054128005,2131936060,2131806550,2628415803,2131658232,2131641594,2005228505,2132067852,2131987562,2063939910,2005936997,1449906377,2132045084,2131849462,2039034204,1884829480,2131707272,3200490864,2886716982,2741218915,2636723700,2440868124,2131628554,1974121490,1973963754,1930362010,1708979677,1404699947,1153046931,2119252337,1763395625,2030223413,1869647492,1796868871,1342334887,2885339420,1973435732,2132169772,2246197435,2132204944,5219415817,3314498661,2437168580,2435466214,2138994585,2130680552,1973507480,1922221555,1862214964,1838875233,1790314587,1764769710,1589206513,2190947913,2132216242,2132215810,2132189760,2132184550,5090624733,2039647610,1973875410,1973467864,5884607314,3169318213,3168928467,2827439044,1841325873,2132261622,1951360145,1673933124,1973190202,5499461971,5172348855,3262129040,2690734411,2132290590,2132279982,2132182684,1979235244,1903837033,1835012950,1691964791,1810454974,5995922399,5430770919,2685870753,2307113564,2175490331,2008686771,1993067820,1925488284,1864799272,3266727072,1830622457,1779900070,1779505554,1571438365,2020178104,2951099654,2803386844,2693379672,2613165393,2212277581,1992179384,1805652452,1991190990,5252830310,2185594941,2041548447,1993051184,1992490022,1990893790,1898245737,1793393673,1777076464,1751199261,1656691995,1628114712,1150942731,2039924232,1991249420,1991693252,1992635090,1821475550,3493071531,2885133791,2839521643,2281985792,1169012315,2174154787,1992392390,1834978882,1771947542,1748137090,1612367363,1991621152,6432928661,6185016342,5967598085,5329731759,3229547042,2164739783,2077983767,2044591827,2036516732,1973489031,1964398600,1914864095,1342866804,2130807962,2130585690,1896334273,2130496342,2132257724,2130700972,3161741004,2130671710,2074636723,2039895030,2038309742,1158236054,2130558562,2130638244,2132234012,2039428600,2144246820,1973056310,2132287884,6126870116,2049158701,2039320394,2038770524,1991283384,1877528125,2045428403,2041411192,2052812217,2048718367,2039884840,2039750512,2036557830,1760730801,1990892174,1934282000,2047836001,3794040801,2088796435,1973735100,1906439531,1881438232,1864134742,1765668245,1750754282,1172505141,1825709367,1760108603,7205359820,6216878537,5647070992,5454201647,3857719032,3539128160,3317049722,2824087114,2661990495,1913708453,1798736903,7276740146,7216074305,7214196327,6890649187,6790360385,6554845368,6417995269,5832639807,5829822671,5782706339,5509965612,5421685655,5339002056,5262233448,5149361248,3509317391,2844501801,2725526801,3125765713,2951593242,5228895290,2093492691,1916825084,1765243372,1614282004,1894238970,1758748503,1640328892,2083716120,3132664607,1809500942,5360910133,1844577772,2107014571,1503773982,1882579600,2596152977,2310686612,1400353615,5945530751,1348463244,1675205021,5652937891,1703394945,5069591738,1797582693,1806780642,1412355774,1219014500,1642628345,1574525211,2190417693,1812431675,1713195262,1782869715,2962497620,1071727923,1665492281,2708305547,1563669152,2192241300,1671981772,1937944922,2816548562,2073349753,2080700821,2103394680,2090404631,2995250591,2672998134,5359964136,3909609627,1869699477,6040412640,3026545520,2734769495,2285390650,2285449440,2094907920,3339723692,3946312399,2246372462,3080270445,2839281002,2620671127,2886705242,2405467050,2867658990,1680849080,2639045301,5212951719,5509995113,2216296114,1797272061,1797272061,1731044841,2679500664,3188450814,2119559412,3504118247,2719754491,1831482061,2338921131,2633855927,2370786680,3722451591,1764127564,1938951285,2230839213,6061323376,5913805303,2110378464,5026192233,1972026001,2462963820,1904768003,2193141564,2880231031,2377018127,2360396497,5712830958,5350825619,3592922582,2755070355,3061411743,1985393152,2165661763,1970770675,2808840650,1967949210,3959213282,5448163881,2662070371,1571037421,5702543073,2843717660,2380613041,2406910981,1909027894,2569950827,2696168312,2180714504,3942946439,2674471072,1974690013,1942755991,1868344435,2463407207,1761944724,1967639143,2185339955,2684415163,3088754380,5144932171,2609601101,1699858945,3355170850,1719253132,5547356961,2212334967,2004062873,2877687602,2807932574,2204883561,1878459917,2010406980,5308670218,2605955345,2991918540,2210878243,3847200576,2435291265,1947300112,2305930420,2497269530,1656360925,3267496057,2153681064,2967826760,1992799765,1896062817,3615192194,5312633841,1893047822,2255025362,2266366124,6200999431,6200999431,1904235783,1658702323,2494474521,3603155154,3951144899,3851854064,]

for uid in uids:
    crawl_weibo_datas(uid)
    time.sleep(11)


