from tasks.user import crawl_person_infos
from tasks.home import crawl_weibo_datas
import time

uids = [1769165581,3229125510,1877674995,2262351592,2485659250,1788911247,5173736345,1658719597,1645101450,6393904893,6124642021,2366532154]

for uid in uids:
    crawl_person_infos(uid)

    crawl_weibo_datas(uid)
    time.sleep(11)


