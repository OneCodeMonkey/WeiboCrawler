import sys
import os
o_path = os.getcwd() # 返回当前工作目录
sys.path.append(o_path) # 添加自己指定的搜索路径

from tasks.user import crawl_person_infos
from tasks.home import crawl_weibo_datas
import time

# 全部（原创+转发）首页
uids = [2471302992,6607564534,6781853275,6585819644,7083513976,2720931423,7318923439,6359305915,6622186120,2188072752,1692534447,2530963143,6677145087,2158643313,5229246817,3996671386,2255024113,6527006890,6583905566,6798307117,
]

for uid in uids:
    crawl_person_infos(uid)

    crawl_weibo_datas(uid)
    time.sleep(1)