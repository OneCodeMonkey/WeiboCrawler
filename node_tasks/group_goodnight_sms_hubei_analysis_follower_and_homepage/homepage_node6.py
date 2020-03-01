import sys
import os
o_path = os.getcwd() # 返回当前工作目录
sys.path.append(o_path) # 添加自己指定的搜索路径

from tasks.user import crawl_person_infos
from tasks.home import crawl_weibo_datas
import time

# 全部（原创+转发）首页
uids = [6334551264,6595691728,6636086606,5705237295,3154242835,6663093618,6621336029,5477989621,6616852582,5565502859,2057057964,5737607439,7070816959,5672516041,5719977898,6480083771,7320494434,7118217226,6592185498,5072460642,3210823162,6276746837,1580752805,6941048335,7098510762,6976839702,5664869585,3049143233,3836493233,5355804207,2856030270,2596009937,5685889979,5162494526,5904751388,6697960380,3740439611,2474423403,6617535293,6201945950,6654402838,5698714120,5574741439,6527330925,3509207805,5948395699,5709616582,2656619547,2885331364,7020341996,5642210395,5036771006,5125486664,6751558639,6787888999,6419028712,5519758151,2173651472,3990260953,5906197377,6728971078,3517284561,6072613625,1781259137,

]

for uid in uids:
    crawl_person_infos(uid)

    crawl_weibo_datas(uid)
    time.sleep(1)