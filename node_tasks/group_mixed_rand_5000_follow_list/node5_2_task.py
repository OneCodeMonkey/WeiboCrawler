from tasks.workers import app
from page_get.user import get_fans_or_followers_ids
from tasks.user import crawl_person_infos


uids = [1404699947,6417933333,1658921165,1947234603,1005949612,2786854774,1864178902,1082618390,1670910223,3788128010,1658683202,1721914570,1965435057,1888347720,1760170871,2076151043,2904696543,2077627203,1689262947,2063525503,5598769597,2374637301,2962284680,2784392294,1813675671,1324170145,2758033765,1106066427,2510365564,2393426671,2881396877,2607011297,1161639981,2091693325,1664919912,2575007681,1898346992,5940154234,2587203083,1541269803,2485035384,2643030723,1773321944,1849040644,2190505627,3170550234,1954352402,2230707943,3299098581,1999386504,2932808754,5592530537,5963821392,1881340453,2583645190,2097127112,5866899501,1733547913,1250145362,1779959500,5997222618,6347741209,2575688237,1962175387,2966001582,3796087680,2659762802,1371391622,1786101113,5105329530,1993838857,1799244901,1903629177,3820049169,1734433024,1834283143,2357391917,5589770214,1966192317,3168928467,6062469482,2551036407,1682189694,5392237610,1735609772,5711382403,1620419577,1735463327,1804421447,1874706794,2884361932,6503703491,1685322974,1767210362,1402055097,1855501681,2232236947,2929121837,5138192332,1802354461,1988524325,1909309084,2722085370,2311240195,2832843793,2438985024,2207927123,2521228780,5079402027,1748658693,1848596804,6386594720,1832149430,1865196862,1686921003,1824307255,1885464213,3720789082,2099038172,2532997314,1663952873,2622320920,2017599435,1768941223,2983199021,1926384035,1766521425,5029139722,1749031877,6255547350,7293785888,1733605744,2450459280,1214598747,2385364931,2171689551,1683252383,1410365045,1986444882,1897270731,1792977475,1643213263,3277844381,1899105193,1784200667,2521550215,3864101625,2272979875,3929517442,2358997013,2100585490,2901779192,6022449694,2171138045,5239705657,1987588365,1849425741,3215724683,1506123244,6694921505,1648923432,1922257385,5853552241,2882681514,2786883000,2185947762,2721987413,]

# 爬取关注列表
for uid in uids:
    result = get_fans_or_followers_ids(uid,2,1)
    for user_id in result:
        crawl_person_infos(user_id)
