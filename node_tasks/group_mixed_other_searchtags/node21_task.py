from tasks.user import crawl_person_infos
from tasks.home import crawl_weibo_datas
import time

# 混合
uids = [2152855062,1791276744,2504232512,1934916913,1785090641,1916304684,2607210115,1834042287,1729659093,2392935100,3821864518,2955765475,2719698392,2680562081,2517541154,2393426671,2365952984,2360343273,2300308752,2078037873,2062715024,2015790407,1903512911,1863951194,1863849234,1771779632,1730909650,1686364867,1678325744,1662801782,1508082365,1361420545,1218096975,1060964911,1813675671,1734452462,2240538983,2152728771,2459123570,1955039682,1589476403,1574476270,1882862180,2560365044,1776604990,1212295855,2348675022,1742783605,1731804004,1439098415,3235121340,2863895121,2569413987,2442438750,2341187197,2075551481,1935483610,1908309964,1904983711,1896050890,1895160434,1889331130,1844676050,1833566550,1825838443,1801450413,1797062545,1784566604,1776522704,1769540487,1725836557,1666511463,1629934981,1947628632,2248421534,2002245983,2253032274,2171440124,2037893395,1872858534,1825215721,1781068377,1779762764,2003550807,2773511343,1958250317,1808072480,1805635111,2429119692,1817614714,3188369951,2952593947,2605160894,2203589484,2108281402,2031753155,2027396977,1999588871,1953989430,1904026743,1886360454,1851061013,1806908805,1798308634,1777288500,1601901823,1320386427,1273594644,2282202260,1253552875,1670340217,1988473214,1884524830,1765549932,2745969062,1996705135,1904752013,1865196862,2017599435,2027873112,1924450671,2798146432,2081619733,3824700912,3293571063,3237757994,2791750593,2772407071,2575859480,2540993880,2501432885,2496915357,2349523665,2150379944,2026055871,1979976313,1923739897,1909580865,1861748560,1777466632,1776553652,1734274820,1729812853,1712973855,1671557964,1398931654,1348152135,1954136251,2283449937,1799907790,2315712910,2027564553,1844271264,1821711923,1677309113,1344578750,1859693150,1927941375,1438909677,2157498482,1769491524,1694543917,1713650691,3031529933,1879245023,1825342510,2712699303,1845977590,3029561102,2962231513,2843852605,2509607292,2481012332,2351800227,2309591720,2276814034,2178992605,2132987334,2122176142,2107872713,2030679077,1981601300,1972887127,1950085560,1937639764,1905021552,1885285494,1876861605,1787980205,1771543377,1750808550,1742832713,1619875631,1131707713,1059384891,2625893075,2328558864,1783216745,1589553190,1901598453,1908600872,1835380123,1771768261,1986233152,1776573422,1998838683,2086048975,3062591287,5459790174,3940291476,3057618127,2839748052,2831448524,2782261277,2546435290,2477417082,2417235653,2354810202,2204059533,2118935630,1986405842,1938950380,1936274250,1909203975,1848789663,1837923334,1832528020,1823337443,1798629295,1798494980,1778928293,1778367457,1766275912,1763659041,1758781805,1737417337,1611192334,1593577594,1221028422,1077159687,1076840290,3169745137,1962325290,3319674401,2187025835,1845363732,1819847435,1768941223,1738532020,1694167517,2072328393,1761847920,1763571105,1850316340,1731262837,2459680181,2699296373,1923705197,1917548180,1893337775,1882572901,1847017393,1746329145,1741067522,1728714870,1698232290,1670843530,1640112791,1421583331,1087444723,2128484451,1908959634,2614891064,1567319341,1898327582,1823607430,2125614652,1971541973,1845437081,3387916322,2123002487,1706495415,2377434182,1794029742,1584286800,2289942372,3331963284,3198833121,3047563391,2862772282,2850911917,2799370472,2786959801,2713882022,2629815483,2509517982,2496903777,2467554872,2319036975,2284289437,2143628232,2013884233,2006610575,1995207182,1950056772,1949665573,1930792810,1930114661,1913750834,1895902415,1895684443,1879532511,1842216587,1725394923,1590855381,1535230721,1302400155,1215939483,2585683827,2294905875,2160017834,1879978765,1852144004,1828322582,1696676384,1628514204,1830310900,2092647605,2000600771,1993639584,1908768525,1937573642,1973716115,2278846411,1853172161,2642510393,3226468187,3171597735,2720995067,2713074383,2704014400,2663646132,2581168522,2385364931,2375973740,2358997013,2300962122,2298653927,2264899311,2257493782,2236025680,2150445042,2051413801,2008788391,1980567103,1962806305,1881110597,1847060440,1839917517,1836008791,1810673372,1756581551,1718799462,1712993450,1684757507,1666835930,1666024660,1654279787,1588366360,1152142987,2403941962,1935490120,2280352720,2390734787,2368472082,2401843530,2118604194,1366409593,2959497157,2031628705,1677154777,3745510070,3127335035,2857792020,2724411022,2640818284,2640082151,2562497562,2390783497,2308826617,2264574670,2250338791,2249160664,2206636353,2189741362,2157332182,2154220232,2131751923,2130992440,2127971387,1970323951,1930349567,1859140934,1839065245,1829308935,1805222015,1748429611,]

for uid in uids:
    crawl_weibo_datas(uid)
    time.sleep(11)


