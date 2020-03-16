import sys
import os
o_path = os.getcwd() # 返回当前工作目录
sys.path.append(o_path) # 添加自己指定的搜索路径

from tasks.workers import app
from page_get.user import get_fans_or_followers_ids
from tasks.user import crawl_person_infos


uids = [
6391556382,3554568437,5055201785,6595481295,2959564503,5455457887,5341987932,5648440201,6274989623,6011393736,3866258363,5669847827,5236810924,2677942503,1262459015,6539421761,6907345479,5960954748,5842707646,3028116775,6190107299,6278239800,1018755935,5794109000,3187640710,6769699748,2675623401,7328954463,2316501084,3753407364,5478807292,1795642663,5569863544,5992925536,6735358452,7029628460,2806932784,6041826024,5997937987,1669963083,6756416358,6708842338,6391450459,7272151504,7212168008,5672487085,5897734825,5708208909,5678036206,2880360930,5729316597,5141879704,6603982361,5883473605,1511648184,6070165085,5590536285,3731018750,7322499331,6802212018,6573296602,3891183956,1764839963,5891891623,1935559123,1786749627,3882738111,6584039678,3236723844,5647194780,7037952947,6104132786,6898257782,3198508155,6818750375,2514112144,6193279716,1364421420,5315514823,6984368360,2825914664,5625763757,5963977128,7025255136,1806273092,5394515153,6520799856,2043993473,6661713959,6180146681,1265505773,6839620601,7211480661,7321286254,6014318655,6087883202,7131323965,3922063515,5888640634,6503864146,3943145515,5303415838,6468204375,2422718850,5813309994,7062253749,7381868927,5932579935,2967749407,5675262289,5963467079,3939974927,5260622499,1830754184,2900380201,5352778037,1219065950,1929946102,6145888523,1787416603,3841537373,1879027962,2399296215,6433066466,5388121475,6599983064,1741534777,6817559166,5620544134,3754794475,6259703496,3226492565,5310640671,2253441157,1227250242,6195643963,7029236578,5984797465,3953760362,6455909992,2921963765,7074057618,7353332060,6820717077,2174306444,6382828011,5745660400,1883893835,3820297391,3202857362,2729098205,5794832248,5657840863,5880325455,1757535027,6173768230,5881915230,5575915115,7233805042,5336829277,3124855093,5217182607,5639841472,6041339925,5876250487,6023325275,6100724039,

]

# 爬取关注列表
for uid in uids:
    result = get_fans_or_followers_ids(uid,2,1)
    for user_id in result:
        crawl_person_infos(user_id)