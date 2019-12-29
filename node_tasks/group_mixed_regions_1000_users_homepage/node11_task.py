from tasks.user import crawl_person_infos
from tasks.home import crawl_weibo_datas
import time

# 全部（原创+转发）首页
uids = [1841561151,1825821727,1791729355,1905612941,1865738484,1589756817,1854029491,1905443443,1947135361,1800179815,1454370903,1463318500,3870985695,1694853844,1315031562,2414183734,2110722721,7310881679,1843269731,2081630457,1771017224,1709194087,1217656322,1954544075,1891503530,2014057793,1742688570,1997472240,1014059487,1640150693,2477322181,2104821463,1500473267,1345105227,1271412485,2407858404,1918322485,1926388003,1945729945,2361533515,1885490905,1708702383,1423746537,1864017744,1611601394,1255267332,1954211393,1932926095,3103617641,2345209253,2418138305,1817013183,2438943773,1678563764,1974855523,1277084255,2605344265,1502684423,1777634103,1096195727,1722615052,1784885001,1784750003,2086338525,1076539827,1489922995,1293562257,2244639837,1738785613,1994504803,1558969515,2088893361,2400539087,2710972261,1994473891,1733942147,1821753797,2300255130,1516658531,1810492553,1913717474,2377175737,1450110030,2313255667,1866404825,2037436835,2430302990,2885288502,1945938487,1631243053,3035797327,1098799032,1516316083,2401912357,2292816484,2535904283,1999903925,1548103183,1282647474,2449685197,1447746227,1614851702,1718739487,1048465162,1368065792,1348523232,2324179713,1813599257,1929961625,1311568281,1912794653,1575406583,1666906951,1626820093,1927712834,2103404217,1835351505,1833161853,1963143055,1947744543,2054797281,2049988057,1910045751,1782013035,1663952873,1424747661,3074850221,5108551457,2007950801,2766169885,1268226757,1893699782,1723167085,1821534193,]

for uid in uids:
    crawl_person_infos(uid)

    crawl_weibo_datas(uid)
    time.sleep(11)