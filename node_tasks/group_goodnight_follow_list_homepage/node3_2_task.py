from tasks.user import crawl_person_infos
from tasks.home import crawl_weibo_datas
import time

# 全部（原创+转发）首页
uids = [6031951233,6307871852,6087823895,2142131744,1769686973,3591074300,6091193400,5319527731,5672503306,5610813150,5866543006,3759928734,5514228783,6396658294,5697464768,6450986183,5644464480,5887260890,6166937391,3713666553,6518297825,1911943907,6297790364,2772843197,2307229910,5311003031,3184416112,2450274105,2023910155,1606122967,2923392855,2437709645,2680446415,2424642655,5995193768,3197452334,5468442772,6296386156,5637853246,3109523567,2132850057,3904481343,5385603544,3260830332,5285471710,7336898681,1644185437,3547427614,5844922885,6474212454,6581020101,5081668113,6570244765,2337882971,6474863383,6673015717,5222990938,3707931963,6479879189,5315994559,2907597153,2136093680,6290555079,3274079220,2189189061,5662774328,5403526320,1654493043,5551601332,5526039896,2876124162,6991900338,5536484751,3199519517,2400760390,5029072973,7165829633,5707133586,5603350555,5024383344,5092813341,3650143440,5715868793,2165547672,6899724139,6288207285,5496352202,6194879742,3006931865,6480485407,6076830469,6604754023,6632380134,5941926734,6539778299,7048199127,6006598016,5254071391,6520203264,3931702025,1954918412,7079559324,5852738287,6687008482,7295657452,6772745522,7111666657,2602408772,6860901319,1964405840,3224068112,5678687030,5827497027,1669786221,5318962687,5270120536,6867826712,6250422335,5822828554,7207075647,7035759976,3537485817,5456744520,5495880788,3995549995,6317997158,5519859829,2400576097,1304263031,7312854871,6503802231,2109732533,5226190328,6527048178,6108365558,5152288688,7028749066,6320802492,5110880750,6477123628,6477315802,5541248788,1928066255,2491722563,6190364970,6613055255,5509209831,5212581597,5053008654,3606753592,5788540686,6368970386,5837763452,1594332271,5170577880,2627056791,3810183555,6465771875,6520049574,5255940131,6027868867,3884490784,6592343789,5267111719,6280654722,6534914794,5835709666,]

for uid in uids:
    crawl_person_infos(uid)

    crawl_weibo_datas(uid)
    time.sleep(11)

