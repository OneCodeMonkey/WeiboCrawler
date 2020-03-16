import sys
import os
o_path = os.getcwd() # 返回当前工作目录
sys.path.append(o_path) # 添加自己指定的搜索路径

from tasks.user import crawl_person_infos
from tasks.home import crawl_weibo_datas
import time

# 全部（原创+转发）首页
uids = [3094060297,
2564419703,
1811053407,
5909191819,
1878643963,
1992698853,
2152971120,
2939186033,
5909191819,
2168608471,
2020501632,
6537676193,
3594646842,
1032825837,
7379124941,
1868429555,
2608107071,
5665264011,
3272850590,
1939425315,
2485614737,
3092980385,
5163203245,
1238166401,
6359564788,
1279840740,
1760705687,
3846348310,
2947506450,
2818143434,
2156856930,
3825121308,
2162949323,
3025806455,
3025806455,
2869798342,
1779709584,
6888689102,
6888689102,
3626863647,
1688857871,
1426994925,
1876273941,
1032825837,
1727956005,
1811721395,
6355387834,
5299732200,
2072172534,
5526933177,
5300382029,
6725383159,
3181874030,
6186021696,
6198888905,
5710864491,
7145283469,
1400038174,
1137028780,
3180437327,
6243305083,
5484615294,
2269156394,
5845360013,
5845360013,
5774091531,
5845360013,

]

for uid in uids:
    crawl_person_infos(uid)

    crawl_weibo_datas(uid)
    time.sleep(1)