from tasks.workers import app
from page_get.user import get_fans_or_followers_ids
from tasks.user import crawl_person_infos


uids = [3471453370,1678513070,5456136573,3796562175,1667717970,5737574832,6473730606,5353688643,2801342001,6065570709,1637290141,1710529242,2716350303,1576103655,2674963633,1651208437,2657596794,1684600274,2649748963,5251312101,5353688625,5132655388,1633809542,1897385232,1894102142,2482499590,5571758125,1153467261,1913374177,2990558463,1937326463,5387091515,2435547921,2848060590,5547781325,3453840754,5353688483,2595827875,1525795577,5353457512,3066968127,2622050322,2855602490,1888378013,2664653933,1224689101,1153976282,5353457397,5848049604,5196870710,1993902861,3874591519,2405001755,3565085717,1748409933,1875711365,5206801339,2552252465,1093979465,2397912363,1863773483,6355115876,1790048444,1784000704,2359815787,2682900473,2346833081,2214546824,5983041661,1682358507,1584124360,1781941323,3783812904,1594372587,1170529743,2641204937,3732699160,1769112935,7168925119,1747388557,2012895010,1989331253,1972427375,1792940074,3405840252,1730967945,3262284735,1233868037,1947401583,2393292301,1930784245,1925957971,5159994515,1914206157,1916121445,1710253853,3975178703,1865510617,1873346740,5866825632,1731316987,5664760724,2500397143,6209786245,1780130655,1727025627,5868292041,2265106971,2907597153,2553129774,1765581332,1358254911,1719559670,1679965494,1174930107,2177660044,5983781255,5237820258,1867633240,1865211733,1866014730,7307873596,5538025272,1509465592,3164953615,5053919679,3878182293,2889078493,2698588482,3208572425,7302969723,2483875210,1921993651,3197227502,1860112714,1838241277,5556070375,2156471065,1791674771,5886704962,1779533952,5537159983,3716977855,1716486430,3279304720,1993572413,1715049775,5582034632,1933339465,1837350124,3798742873,5353688555,1554042831,2401266852,5210612592,1300566840,1884687355,5209163893,1863881291,1787294713,5379778889,2755961661,1824986193,2282787833,1696441014,3692543982,1921142815,7220614883,]

# 爬取关注列表
for uid in uids:
    result = get_fans_or_followers_ids(uid,2,1)
    for user_id in result:
        crawl_person_infos(user_id)