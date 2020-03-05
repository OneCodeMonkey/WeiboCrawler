import sys
import os
o_path = os.getcwd() # 返回当前工作目录
sys.path.append(o_path) # 添加自己指定的搜索路径

from tasks.user import crawl_person_infos
from tasks.home import crawl_weibo_datas
import time

# 全部（原创+转发）首页
uids = [6724825036,1751690473,2733970672,2957052213,6778638552,3194573440,1787416603,5342778422,5238917438,2111539960,5985336590,3477702432,6313074608,5915350423,6782552458,5843060726,6069335857,3838191216,6346151457,5513255694,6572587348,
]

for uid in uids:
    crawl_person_infos(uid)

    crawl_weibo_datas(uid)
    time.sleep(1)