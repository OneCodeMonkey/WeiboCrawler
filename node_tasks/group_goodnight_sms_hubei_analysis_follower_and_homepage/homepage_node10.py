import sys
import os
o_path = os.getcwd() # 返回当前工作目录
sys.path.append(o_path) # 添加自己指定的搜索路径

from tasks.user import crawl_person_infos
from tasks.home import crawl_weibo_datas
import time

# 全部（原创+转发）首页
uids = [6229276754,2162437430,3678281167,3665329565,7209349482,6680501307,6435528536,5253867292,5810131828,7205315081,6433877377,7202721949,2526456921,7318450229,2528296385,3908442225,5501028610,6703820996,6184780995,5631532047,5625796972,6363126945,3033698835,6588031931,6160671796,6109839962,5288300059,5538294083,7169422657,5094464314,1795469043,2464624063,7275623927,7168272176,6690396515,6587254272,6295924259,6027965784,1967394531,7197968999,6125710661,3145403344,5532227350,6022612236,6617315599,6602416203,7015828036,1789755151,5977153646,6756476256,7014023132,6422451468,2658773122,7320900598,7345589216,7080628790,7192061176,6574021075,2507785781,6041302549,3537952290,5873747775,6126537301,5080096342,5971158125,7372916779,7214482131,6308867694,6929998784,6203181552,5238953052,2670040931,6616488403,1647771245,5426619240,7059265803,6596633581,7109479051,5505616081,6573444074,6573820270,1764048363,2805852013,5123312320,6045977425,7088845012,2667687981,6131995318,3887961347,2837922381,5892188576,1838096081,5527479657,3733518350,5264541788,3787703953,2102448443,6468957274,6665192157,5610364995,7333213831,3416181054,6348183070,6510085527,3086161515,6078600381,6398152716,1966712845,6177277661,6012583982,1691182591,5430423163,6893469475,6526304530,6677362040,6486940476,5379264671,6000095433,2252929114,6741023146,6596853430,7170189673,2463394294,5694457481,5630559790,7080432742,6508427896,1461011292,2347551763,6617905096,6523828534,3194573440,2439149105,6456199574,6666583624,7306752238,1690922735,6185359960,3265963967,5874773049,5194327823,3584417023,6589856388,5494430736,6865580985,7286391254,5688529798,3224911357,6693872145,7105666407,6782731420,5908119746,7332050624,6092166199,3597060041,6189527115,1759454437,5688889041,6211947927,5804314265,6310373420,5246311782,7396282316,3181329350,5776472144,6222955888,5126250222,
]

for uid in uids:
    crawl_person_infos(uid)

    crawl_weibo_datas(uid)
    time.sleep(1)