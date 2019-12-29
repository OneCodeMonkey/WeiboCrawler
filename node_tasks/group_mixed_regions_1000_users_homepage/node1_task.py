from tasks.user import crawl_person_infos
from tasks.home import crawl_weibo_datas
import time

# 全部（原创+转发）首页
uids = [2417202727,2134832367,1816621420,2369728412,2478831610,2659803573,2253559485,2631520302,2307147964,1940879643,1942938135,1903448565,2474155012,1676228255,2278878984,1438914670,1440399900,2698399794,2567522387,2944075771,5254908940,1761705425,2608374731,1733479912,1784408334,3828391333,2831123210,1890024155,1861373642,1898083900,2714956133,2300272455,1988716513,1769393012,2062473763,1966183277,2337421170,1908160477,2328032890,5392064524,2663646132,2653366142,2018373853,2213710683,1943298721,2196221821,2881026622,2785338562,1733888472,2017014787,1788779234,2436012790,1971661737,2330116642,1996738055,2454804390,2172565597,1770298100,5201906463,2677900253,2574134201,1881678014,3481658950,2412072261,2335739534,2647594091,1944049123,1763959345,2630626054,2591819575,2237830172,1938091653,2270919810,2669461983,1566943613,1823733240,2948928900,1562178530,2034928232,2883818772,2175867590,3283357565,2854237832,2317183600,7311192563,1087547680,1762473174,2149527414,1918124565,2256049322,3016550401,2108447624,2301279157,1570244683,2074513654,1972005065,5671706782,1686995031,5795867710,1791263501,2081384012,2171974913,3109892545,1840458872,5292430532,1881623182,2736401980,2365903833,1848412732,5936470308,1686363945,2483673020,2790831581,2267082283,1701961793,2470337000,2480348627,1686117267,1868965883,2204719043,1743494685,2391938487,5467047322,2823428385,1785741282,1962092531,2289711461,1763636384,2134838637,1073395183,2389433275,2432612373,2287189120,1657373184,]

for uid in uids:
    crawl_person_infos(uid)

    crawl_weibo_datas(uid)
    time.sleep(11)