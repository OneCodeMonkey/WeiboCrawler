from tasks.workers import app
from page_get.user import get_fans_or_followers_ids
from tasks.user import crawl_person_infos


uids = [1226612814,3141280087,5098893504,1866927415,7222988310,1930186570,5409790954,1646698493,1403493257,3847997883,1853227831,3939036953,1763353391,1134742570,1638736854,1106066427,6189588297,3220837945,5683551342,1792792931,2675112513,1933911417,2062642501,5590130879,1722292841,1769090461,1661427094,6533687677,1782581565,2087394164,1732910753,2088923513,3553076145,5927354800,1831480474,1849720980,1893699782,1717801074,6332063583,1888132163,5567662698,1984113603,2181217974,2564590731,2372103365,1948748630,1724731720,3211696412,5651158657,1463919924,3859330024,2737890997,3333874520,1913897262,3923544474,2809739854,3211542100,1698232290,2301679453,1879373394,1347949163,1866186067,1741419277,3262542124,2704825117,6030182039,2949504577,2719698392,1943910207,3252495162,1308455682,2194098132,1597179222,2201801034,1410366070,1848003500,2434609484,2966156990,3574972741,6150014074,2103948912,1990937211,1789042740,7056215092,3223246051,1547711612,1706521843,1768346942,2198659273,5095933262,2710794531,]

# 爬取关注列表
for uid in uids:
    result = get_fans_or_followers_ids(uid,2,1)
    for user_id in result:
        crawl_person_infos(user_id)
