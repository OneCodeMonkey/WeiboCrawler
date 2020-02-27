import sys
import os
o_path = os.getcwd() # 返回当前工作目录
sys.path.append(o_path) # 添加自己指定的搜索路径

from tasks.workers import app
from page_get.user import get_fans_or_followers_ids
from tasks.user import crawl_person_infos


uids = [
6492039360,5873767369,6097053548,1857428312,6628899733,1959479215,7027142894,6247163992,6322645550,2010427683,6301484655,6068129377,1415502354,2581173200,1892462262,5625630478,2528154830,7321181196,6652949845,2478204254,5688334861,5261451151,1920705942,3939982750,1903812461,5621572158,3938429007,6262795950,7200086188,1416630715,5151510175,6974549100,3939498674,3679952680,1494647095,6662055355,6348965759,2020298691,5319323773,7044527156,5436177977,6868369653,6681470978,6455856378,5465934035,6598466519,5683561516,1918291213,6326440804,7024512034,2427954984,2760523463,5472840129,1106840607,2637830435,7146532608,2477568231,2554250377,6467969712,7268078800,2838956177,5388860992,5774081030,5865978022,2407852711,5681580241,7324217412,6468271665,3291275294,6646203669,6066227496,2297802803,1746381580,1817675355,6557004147,7103749314,7273191406,1612188637,5577026939,5267899109,5728455412,2650582017,2186842532,1561727770,6440240860,6443153038,5888369076,6633317007,6451423825,3838191216,3115914465,1831270354,5598157631,2664126420,1737868010,3687795825,7290221793,6993750269,1750035633,6307184043,6467969174,2932315804,5310269484,1339049975,6198715772,7262788904,6613521099,2377347013,2083194057,1663767722,6635783101,6596915463,5194171260,6630243136,3220297372,6347852429,1667344964,6455898065,5736430260,6520528608,1721281267,5845865803,6017262128,5382877582,6616233225,6648275535,3938612994,1767803802,3761985185,2294353593,3746837102,6346151457,6612221188,5276101510,1674081491,3941431580,6779702424,7169773819,5513255694,6347850902,3151034964,6904450593,5107204392,7285240346,7154284881,1572093625,5645756008,2598771897,3947733039,6342529957,7217563880,5626772678,6244228570,6264819982,3566822912,1826631213,6766452476,6784819525,2856374412,7189149495,6466433374,2732417907,6045528808,1826103883,3635938360,6440234560,6850486145,

]

# 爬取关注列表
for uid in uids:
    result = get_fans_or_followers_ids(uid,2,1)
    for user_id in result:
        crawl_person_infos(user_id)
