from tasks.user import crawl_person_infos
from tasks.home import crawl_weibo_datas
import time

# 搞笑榜 https://v6.bang.weibo.com/czv/gaoxiao?period=month
uids = [1764222885,1713926427,2709577332,5700379397,6593871464,5888328091,2111145965,2510980482,5575762010,5622004557,5321383497,5662234502,2984094261,5220839587,1852220282,3502967407,5532084803,5842225215,5153273079,5765378903,6700634492,1551631093,2726698224,3173611413,1791867263,2244367010,5450071244,5974585848,3648873152,2182038504,2187272842,5675321034,5150833941,1644395354,1750796960,5711070913,1939822100,2236459197,1134796120,5780240684,5643112633,6177529873,6224564922,2337814547,3164835813,1357426902,2718604160,2968975055,5537647515,5371249259,2179447851,2708212105,3856942632,5539627669,1720464350,1999601491,5727942146,1748182764,6219659855,6224097333,5881123708,1642635773,2958527367,2562658331,2156393955,1779595382,1096778425,2614543117,6427203514,5328650840,2140284871,3938797402,2435939794,5718310125,5055104198,3129816345,6180213612,2293424284,2763530405,5870251637,6323447943,2438867634,3440325930,2485425080,2488424752,6434212347,1266709574,1740577714,5871895617,3542297544,2865367644,6433036893,1653957693,5634753105,2970036311,2691939561,2400966427,5340337769,1615743184,5874715391]

for uid in uids:
    crawl_person_infos(uid)

    crawl_weibo_datas(uid)
    time.sleep(11)

