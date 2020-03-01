import sys
import os
o_path = os.getcwd() # 返回当前工作目录
sys.path.append(o_path) # 添加自己指定的搜索路径

from tasks.user import crawl_person_infos
from tasks.home import crawl_weibo_datas
import time

# 全部（原创+转发）首页
uids = [2399296215,5388121475,6817559166,5310640671,2253441157,6195643963,7029236578,5984797465,3953760362,2921963765,7353332060,6820717077,2174306444,6382828011,3820297391,3202857362,2729098205,5657840863,1757535027,6173768230,5575915115,7233805042,6041339925,5876250487,6023325275,5342778422,7069410456,5285628847,3003436854,5710258929,5891298766,5270965275,1722624523,6290893773,6444573982,6271978853,5885626467,5182428076,1869739183,5238917438,2462179665,6081881862,3265901404,7238913947,3009452865,6707489967,5948678023,2010243561,6612537764,1720447285,5853273337,5969788694,5750777403,3483950395,5692477045,1685228542,6568028653,6751544450,6721976010,6507125257,6726605794,5329057195,2418476714,6335004219,

]

for uid in uids:
    crawl_person_infos(uid)

    crawl_weibo_datas(uid)
    time.sleep(1)