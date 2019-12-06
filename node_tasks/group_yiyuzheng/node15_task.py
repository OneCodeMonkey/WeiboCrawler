from tasks.user import crawl_person_infos
from tasks.home import crawl_weibo_datas
import time

# 混合
uids = [2927640562,6055572417,2432298553,6464069410,6514818250,5886397651,6544320629,5363173480,6760006080,7211952647,6409919702,3190171104,5669378334,5246047464,5892340370,7331884686,5680420430,5902229064,3916056328,2435081372,]

for uid in uids:
    crawl_person_infos(uid)

    crawl_weibo_datas(uid)
    time.sleep(11)


