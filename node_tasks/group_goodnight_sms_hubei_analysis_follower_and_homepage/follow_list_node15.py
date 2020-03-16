import sys
import os
o_path = os.getcwd() # 返回当前工作目录
sys.path.append(o_path) # 添加自己指定的搜索路径

from tasks.workers import app
from page_get.user import get_fans_or_followers_ids
from tasks.user import crawl_person_infos


uids = [
3045135161,5702332713,2294232677,5970548924,5249971030,5639967192,5594801453,1415111912,7366555831,5035800389,6866610452,1926019691,5429126212,6666887608,5817341503,6964671947,2704770111,3214180870,6241868003,6872921096,6783155008,1257966900,6279827934,6720770323,2390714700,6148591763,2241403807,6733467658,6634088306,6604790267,3176571067,2250678460,1934028467,1822385741,6881133040,3022753487,6603419009,5797846219,2166081070,6441049353,1801752820,1814141225,5489762979,2207699090,1559535501,6855475574,5541701152,3392470100,5401735816,2708051685,6673965161,1304128417,5839730620,2084063841,1828316007,6239661310,3372651254,2175316862,6616243823,1669730072,5691060009,1014304460,7157380537,2509246241,5283311472,1159223902,2871694843,6008578068,3085545381,1075813283,6178723315,5749282354,2091325613,5604557601,1842369863,2111539960,3164166503,1643946223,5431105350,6320744517,6285900666,5270961620,2653211212,2845215040,6465970389,5133216821,5352384655,6582969950,3592557393,5717189453,1763403640,5235439078,5979867688,6637875415,2565431121,3967758786,7362813914,6832454652,6440194700,1764484980,6520738532,3657949462,5325457871,5982005914,7363427210,6523803062,7041926679,1918749907,2812182415,6312047210,5781344220,6102870573,2718805725,3936951028,5141647430,5261687659,6120451312,6039940718,5856813803,5631933411,5946128537,7358634213,1970028155,6257693645,3160966163,5650019186,5602498223,6898335283,5341613725,5589354792,1695785472,6434621918,5499257081,5375123169,5851176261,5864109200,2364655455,5268739281,6994891517,5976176894,5963813759,1619291043,6158663130,1950860931,1939481117,1801604455,6459175399,3467871994,6277435211,1659709970,1777469711,3592599667,3858422467,5533142665,6189334432,6583795311,2669145361,6080389572,6128453723,3480221284,7208962079,5985336590,5144974339,6008922890,5658308109,5636091829,2880630645,

]

# 爬取关注列表
for uid in uids:
    result = get_fans_or_followers_ids(uid,2,1)
    for user_id in result:
        crawl_person_infos(user_id)