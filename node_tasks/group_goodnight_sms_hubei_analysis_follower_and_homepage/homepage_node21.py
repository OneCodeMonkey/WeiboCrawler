import sys
import os
o_path = os.getcwd() # 返回当前工作目录
sys.path.append(o_path) # 添加自己指定的搜索路径

from tasks.user import crawl_person_infos
from tasks.home import crawl_weibo_datas
import time

# 全部（原创+转发）首页
uids = [5970553450,5996836999,6171263110,6487179972,6787879390,1080651342,7290692821,6730482478,2291267361,6184107372,6652949845,3291275294,6646203669,7103749314,7273191406,5577026939,5728455412,2650582017,2186842532,1561727770,6443153038,5888369076,6451423825,3838191216,3115914465,1831270354,5598157631,1737868010,3687795825,7290221793,1750035633,6307184043,2932315804,6198715772,7262788904,6613521099,2377347013,1663767722,6635783101,6596915463,5194171260,6630243136,1667344964,5736430260,6520528608,1721281267,5382877582,6616233225,6648275535,1767803802,3761985185,2294353593,3746837102,6346151457,6612221188,1674081491,6779702424,7169773819,5513255694,3151034964,6904450593,5107204392,7154284881,2598771897,

]

for uid in uids:
    crawl_person_infos(uid)

    crawl_weibo_datas(uid)
    time.sleep(1)