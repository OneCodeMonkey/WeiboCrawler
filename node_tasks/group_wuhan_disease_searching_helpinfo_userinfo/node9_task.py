import sys
import os
import time
o_path = os.getcwd() # 返回当前工作目录
sys.path.append(o_path) # 添加自己指定的搜索路径

from logger import crawler
from tasks.user import crawl_person_infos
from tasks.workers import app

uids = [
    2889273104,
    2713131601,
    1847123567,
    6275255374,
    2645029644,
    3317199863,
    5313519051,
    1649173367,
    1948349457,
    5692840475,
    3515639462,
    5577766918,
    3991154489,
    1906592371,
    2006722532,
    3042851262,
    2553737234,
    1340711717,
    2006337157,
    6053810483,
    6916860737,
    1917050314,
    1908928063,
    6068931062,
    2783265085,
    1919439871,
    5526939978,
    5883543871,
    3928511449,
    6524418720,
    2110254375,
    3185528391,
    2475451187,
    2143947405,
    1974576991,
    1723860137,
    2739211877,
    7182841644,
    1720962692,
    2732501400,
    1999349677,
    1254344604,
    2022364304,
    1663072851,
    1974576991,
    1618051664,
    3551462275,
    7372313440,
    2565811051,
    5733054424,
    1896650227,
    1749588581,
    5625104794,
    6406939444,
    1663072851,
    5506906732,
    6119593135,
    5912224664,
    1685200230,
    3871460891,
    1355859131,
    5375368884,
    2626472803,
    2113534174,
    1905964443,
    6469491058,
    5767662194,
    5074438148,
    2620648747,
    1064443200,
    1691745032,
    3245288485,
    6164918531,
    2448706831,
    1876464975,
    1882122804,
    2101918757,
    2433451352,
    5593534365,
    2482121251,
    1668926483,
    2607972104,
    6115513885,
    2000677085,
    2802864755,
    1895394815,
    5260965237,
    2575739902,
    2144661353,
    6620897638,
    2587896052,
    3952517679,
    2279872037,
    5533548092,
    5324777856,
    6093210519,
    2552045714,
    2203282867,
    1753152755,
    5262624571,
    5320051585,
    6862060973,
    3262278202,
    1568450860,
    6096220403,
    6174509848,
    5119857361,
    1420157965,
    1837869620,
    6571723664,
    1503818667,
    5461921176,
    2663176373,
    1784473157,
    2800456272,
    3867969969,
    1910695630,
    6073537622,
    2524318540,
    2458438205,
    1921838932,
    5646277030,
    3502801212,
    1455543965,
    1034499855,
    5241454796,
    3446140882,
    1228404891,
    6019389480,
    1053953693,
    2266137860,
    5854208823,
    1706406001,
    1239742074,
    1831401710,
    2805835370,
    1728112247,
    5455980591,
    6068931408,
    2694355870,
    6636571890,
    5040955225,
    3361952722,
    6426047298,
    1274460913,
    1773100522,
    3928511449,
    1288496124,
    1881270367,
    5077694496,
    3722844281,
    6066193547,
]

count = 0
for uid in uids:
    crawl_person_infos(uid)
    count += 1
    crawler.info("count:" + str(count))
    time.sleep(1)