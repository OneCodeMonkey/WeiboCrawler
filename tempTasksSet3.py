from tasks.user import crawl_person_infos
from tasks.home import crawl_weibo_datas
import time

# 人气V影响力榜 https://v6.bang.weibo.com/dzs
uids = [1822398137,3217179555,2929571482,2891529877,3099016097,2995631244,2150511032,2057769762,2259906485,2123664205,1689423542,2686579097,2481092927,2430259303,3167305545,3069348215,1788911247,2804610542,1771295435,1748852693,2343372547,1098618600,2576867470,1799473445,1086233511,1843070674,1895964183,2530520950,2700797874,1898127921,3029885921,1757573407,5098547539,1705901331,2359037744,1687442081,2792993754,1764523734,1470809487,2619981000,1750513063,2185608961,5235744929,3580163954,3163213212,1706500860,1672335485,1236355832,1658719597,1751775581,1694061470,3517499214,1820578701,2090683994,1994712500,2192919030,1771140437,3819363678,1293472177,3030975747,3190764044,1680078915,1994998151,2620694653,1073238785,1292380541,1647415197,1286189071,2431974872,1798716414,1581391555,1134233684,1737520307,1580275663,1976802917,1859483112,2645249603,2010721297,1781394465,1868306103,3551039873,1254926960,2493678981,1723261380,1800591743,2344328334,5127225727,1298977342,1344386244,1067572881,2571906604,1744188571,2796627290,1069384980,2175145141,1403742220,1646348343,2138029773,2675322102,1700640805]

for uid in uids:
    crawl_person_infos(uid)

    crawl_weibo_datas(uid)
    time.sleep(11)

