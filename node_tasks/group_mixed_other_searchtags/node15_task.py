from tasks.user import crawl_person_infos
from tasks.home import crawl_weibo_datas
import time

# 混合
uids = [1764134377,1879726205,1758757131,1786274323,1738044782,1818711992,1671021017,1780402225,1597416573,2727291480,3623511233,2661556743,2633837963,2595789234,2230846792,2009056877,1818711992,1671021017,1780402225,1597416573,2727291480,3623511233,2661556743,2633837963,2595789234,2230846792,2009056877,1971905563,1969633980,1933422755,1931127777,1903308911,1894398484,1890247902,1870699565,1721277237,1299029454,1894700127,1746970744,1630410031,1941755613,2842102902,1474885352,1967566343,1776180371,1909240057,3612921060,1895223594,5833049307,1440949175,2407435923,1759022583,1627098942,1881933087,1907948341,1845055581,1236613132,2092167567,2142755781,1977174111,1645078134,2179529001,1863564995,1652770615,1668342443,2085647453,2908939742,2694154822,1699755675,1801878443,5984315934,1648251661,1400188987,1375720175,1625667971,1843220942,1785636123,1752207202,1731614693,1721914570,1869463074,1893449127,1568658024,1616738551,2589397465,1855983173,1965908203,2393385474,1684584722,1653174303,2203868005,1931013757,1911226065,1873885110,1740311967,1710200862,1258599792,1186005141,1573274954,1613959474,3853656615,1908570101,1801415285,1687790081,1905612941,1950614730,1751131404,1304090535,3550641941,1711482562,1724446431,1867728674,1788893061,1758065487,1422434287,2192594631,1861856607,1133239157,1342652254,2212993725,1911320431,1773739467,1571263502,1422050993,1631927454,1809430750,1834544727,1970151997,1841779644,1829106194,1795086802,1728713022,1689458357,1646204945,1174082003,1936078791,1726971960,2427313583,1990842814,1321480403,1948522930,1947009073,1624934042,2107841202,1886586901,1796628843,1776667371,1771471340,1719526687,1712459807,1308544493,1797468031,1925098691,1941213635,1859304802,3182219832,2623344547,2177594763,1849579932,1845103242,1808434402,1801629197,1778902957,1692421825,2389283717,2178976353,1676716502,1770483465,3693691772,3023482681,2733486447,2340170255,2020453753,1777072564,1774180345,1766747684,1743151133,1738702237,1695455005,1766737524,2294818170,1053527323,1685898004,1588458411,3969426898,2194904260,1890796344,1792431511,1787252041,1726175497,1701934314,1693958713,1675744945,1652384930,1568454292,1217593824,1161639981,1073877643,2692812192,1750744691,1723053485,1678679797,1959578793,2332441944,1991790225,1884898510,1851324993,1731391025,1702954931,1199748092,1073896671,1062502813,1763450697,2786753782,2299586237,1864092974,1781969797,1779066332,1741474271,1696654744,1351573541,1216599997,3988411655,1752658234,1782610291,3138624315,2712437187,2539560693,2325048630,2247473447,2118402557,2108733452,1928025085,1865738484,1846463912,1791715410,1737740081,1737361271,1700427923,1851090475,1031152364,2522652182,1790697911,5127836182,2645705601,2636845887,2440344775,2291104040,1956806120,1950446234,1935792050,1912997391,1892044900,1842937884,1791215487,1750889703,1739459747,1737714277,1710353742,1306036045,1279052363,1889922031,1781047702,1705464470,1682817391,1775152757,1927663321,5110812267,2470459735,2301584785,2214096531,2136352855,2113724650,2061022131,1881495962,1788089237,1768510200,1745786900,1272375060,2139429884,1926160825,1748874275,2397021705,1821606432,3196734842,3167988572,2425737104,2395011800,2104909377,2062642501,1954544075,1949475174,1915643585,1655132001,1654505260,1220663432,1215117761,1168610950,1066614965,3491423957,2653177321,2040834630,1948106443,1849495767,1846905617,1945351977,1735514965,3277408025,2585245817,1237709377,3554719374,2970804137,2684906141,2521774190,2300629402,2293678244,2249723562,1919724573,1670546093,1291002927,1790559675,2035867051,1982235770,1934591923,1926562957,1916587567,1916057493,1894952183,1883640352,1859608450,1921520735,1825733741,1803327863,1661307845,1073941635,1691375530,2469002870,2100906637,1697478102,1871734685,2962473473,2464831647,2334590794,2203624672,1999509775,1893903274,1768655327,1686464862,1601362513,1561536952,1779166203,1830005631,1402708432,3288061714,2402970931,2391931560,2368073677,2038941630,1962275412,1959772425,1940600447,1073385670,2437303200,1730347055,3514626961,3381268000,3279695935,2647806111,2114069491,2028008862,1883737874,3522017440,2701436343,2126152702,2053436395,1417106165,1784468934,3710143562,3229895303,2420692962,2141417694,2018145395,1978839097,1886324761,1537603527,2300841422,2609279503,3238279440,3134565015,2810419295,2061135073,1864189161,1853758771,1733852905,1768396550,3138579730,2787534243,2520195760,2510285290,1757137103,1215332672,2161912932,1783997590,6479977847,6196530691,5231318716,2199085095,]

for uid in uids:
    crawl_weibo_datas(uid)
    time.sleep(11)


