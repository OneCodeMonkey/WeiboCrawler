from tasks.user import crawl_person_infos
from tasks.home import crawl_weibo_datas
import time

# 全部（原创+转发）首页
uids = [7277973084,6312124617,6981581506,1935838260,2630736025,3990904213,5027218867,6105827498,6610137440,6355392628,1954457141,5404033004,5348909277,2489704005,5240153476,7043974248,2608117793,6144034518,5387562752,3655177525,2111238445,6725006120,6660433726,5736933972,6000085481,3108253293,1809854670,5377305790,2130087731,7303460251,6207205494,3022960847,5162300463,5149731628,6128849525,3655204175,1611464635,2323732245,6294529134,7281790474,5901760769,5991071548,6156560702,6621138748,5909930501,2249725083,6003527828,5348990657,5511249660,5635971251,5673981814,6992727596,3128410457,6304825068,5769571951,3856875106,5696367255,5983018063,5966418374,5783046272,5614064713,5537048782,5574217213,7052215261,6646497952,5173750391,6355862675,3158296385,7009033742,6237807424,5206773553,5753796971,7075382644,5866618940,6457787169,6596848580,3118380203,6431770824,7150660651,1752901444,1769748327,3923647362,2045350857,5799747843,6341958304,5674411714,5672604433,5977165196,5282211145,5904237958,5923495015,5837578340,6275198674,7333849245,6662170282,5649254769,3703057037,5863945563,6608042174,2098480725,6614883162,5657175740,2454688302,6768119237,7339507334,3610868947,1917217691,6540815051,1698320327,5130674284,5679062117,5224133992,5542781041,3932508127,1725454117,6035756696,7267988503,5663622659,6460505804,3529065523,6303774110,3149676542,3294264524,5271683572,1577284193,7147987680,1879858180,6485267452,2169010523,2157902855,5173930368,5783336250,3810101585,2796990993,5546901020,5850909460,1816120344,1291232174,6614105472,6292674238,6569805754,6415087858,3824176443,6598566265,7014812850,6142032082,5727342536,5945869490,5681483407,6651931666,1842709023,6372534330,5983950800,2856337660,3316557491,2672271383,1750459421,5404204388,7350020397,2365135367,5380291413,2019587924,2721828642,5330408965,6141906293,5455086851,5496605832,]

for uid in uids:
    crawl_person_infos(uid)

    crawl_weibo_datas(uid)
    time.sleep(11)

