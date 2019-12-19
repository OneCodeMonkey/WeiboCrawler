from tasks.user import crawl_person_infos
from tasks.home import crawl_weibo_datas
import time

# 全部（原创+转发）首页
uids = [3836565056,5127123602,2142202970,5127176963,7269533414,2168490463,1923000251,3005667805,3084769675,5984440985,3091089532,5344644518,5876158588,3321382160,5837771444,6357355508,3978337205,5482009195,6428204510,2529209182,5658744930,6537749509,3803532125,5387343076,5342502818,6618786797,2399412541,2766015531,3544987743,6099018308,5689077155,6577353003,5235045586,5393399338,3362120102,6622157138,2771131731,3024342333,3893734348,5683887751,6056737469,5559033683,5661952854,6008798764,6458199324,6835385344,2853014795,5768306450,5503307296,3233887262,5312056085,6345049958,6571098393,5622590137,7151791216,5332325063,6095353471,1934733073,5800830407,6970609736,5893645858,5979645726,1357007791,1681365923,2612447185,6361489784,5681813400,1819758604,3355593970,6622993185,5055069116,6981201530,5288392996,6116685896,6269245150,6460418768,6056718196,6132026152,6379485166,2674073720,6118550352,6865562228,5591305653,2676950902,7194048972,6048528064,6255466760,1805770243,2746634292,6580628569,7230756634,7350162772,2104906745,3199634502,5483809257,5368788148,2151589567,5179472859,5976714416,5495263180,1380403024,5389926164,6104354677,6310486094,7265822511,7002776950,5574900857,6364665503,7337202387,3014117630,5237495779,5399156455,5675082528,5227114754,2889146903,5708989616,5108634091,2624329495,2164799405,5146433735,1749615601,1560983152,6316755631,5516556455,1792950272,6577276289,2164575733,3712279687,5320697288,7153579251,6448427388,5235789376,5242681937,5691608521,1034820144,6448214353,3029126183,5527180656,3226975991,1011202981,5243310504,7002176295,7345856261,6394989725,5280487177,6802053826,6275159200,6178117737,5996196488,2279697173,6920274317,6049772799,6393854608,5373730981,1673903041,5481828829,6044404346,2056903847,5762618514,5307878285,1956832807,2331122847,7313836075,7316895318,5690110433,1791960081,]

for uid in uids:
    crawl_person_infos(uid)

    crawl_weibo_datas(uid)
    time.sleep(11)


