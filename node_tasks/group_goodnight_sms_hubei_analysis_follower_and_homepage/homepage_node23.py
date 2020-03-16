import sys
import os
o_path = os.getcwd() # 返回当前工作目录
sys.path.append(o_path) # 添加自己指定的搜索路径

from tasks.user import crawl_person_infos
from tasks.home import crawl_weibo_datas
import time

# 全部（原创+转发）首页
uids = [6114793827,
1732717474,
1654828243,
1614827221,
2247438347,
2247438347,
1032825837,
1597050477,
5522904007,
2901604625,
5656310474,
2470240801,
2470240801,
2470240801,
2269156394,
6888689102,
3192613274,
5312659809,
5312659809,
6051408035,
2688568705,
3098216024,
1162301702,
5994404851,
2905577167,
5536359270,
3626840292,
3482763350,
2818143434,
2657835897,
2651436820,
3187699637,
5641652884,
1822631253,
5891847019,
3209389877,
7378623969,
6989701026,
1887949730,
5732212045,
2811059104,
2697736197,
1447988533,
2269156394,
1762095714,
5706679063,
1098142302,
1733133384,
2781121994,
2485821241,
1412353242,
2327501342,
1644334623,
7003322699,
2731098450,
5252939994,
5503782321,
2080054185,
2485821241,
1144962445,
1144962445,
5159548250,
3935184245,
5500227844,
1926224490,
5257663981,
1032825837,

]

for uid in uids:
    crawl_person_infos(uid)

    crawl_weibo_datas(uid)
    time.sleep(1)