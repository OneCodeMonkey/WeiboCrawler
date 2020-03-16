import sys
import os
o_path = os.getcwd() # 返回当前工作目录
sys.path.append(o_path) # 添加自己指定的搜索路径

from tasks.workers import app
from page_get.user import get_fans_or_followers_ids
from tasks.user import crawl_person_infos


uids = [
6888365246,6008076407,6470310392,5639807956,2385251225,2622947091,3167156852,5816411304,6613014938,2004865903,1785009011,3817196275,6597074180,5948788820,3842539769,3928067699,5706782811,5139226538,1846031865,6684764911,2513106522,3894962149,5836368803,6352632798,6250132302,6346493066,7218919092,6334949790,5663210078,7305416989,6582679378,5841730031,1196355121,5406589752,2672905775,3457704122,7016088981,6754405878,7317888598,7315560007,6022076339,1497719590,5648930450,6774827138,6993692578,1824141631,5889966958,1200720980,5848347116,2677164660,5285670640,7305830528,2810440892,6637816928,6777882427,6606650870,6713310961,6654435901,5896913481,1317541812,2495760402,6731919264,6023946618,1881366712,1436830497,5999734539,1846022523,3936672961,1665297312,5727423737,5504640569,1027860121,6537968678,1325724721,6112699136,1677049641,6746236149,1727993710,1742438425,6575767926,2579670844,6010747954,5580094894,5657445465,6870975361,6744748111,5768131689,6447701385,5391463444,1229133867,1381054143,6524029826,6727871130,5782310562,2454214930,7250861650,5675530817,3720301525,6582256316,6689427030,2362160770,1709807225,7345873085,7200522138,1771548563,6038203298,6472539403,5586298650,6023523647,6397847003,6067544640,3995385049,1753073471,6748396271,7015485924,2673644711,3942192001,1736320207,7389592749,1242904953,3894128595,3924471005,6080068376,6112682145,7183225300,3036701497,6204365426,6209716437,2519414770,6187562801,2160342870,6571532151,6601013750,5885446977,7105560970,2463497557,2626680471,5799445043,1996529893,6217526601,3143111350,6056869300,5239082918,6779204444,6606199930,5024039378,5145644115,6288874934,2608750393,7034935591,6778221990,1618407822,6099125683,3195701420,5750334644,2652020190,1021293417,5607032973,5990946981,5143454264,3347970184,5567380656,5436605897,1736419945,5120942302,3718700677,5223157577,
]

# 爬取关注列表
for uid in uids:
    result = get_fans_or_followers_ids(uid,2,1)
    for user_id in result:
        crawl_person_infos(user_id)