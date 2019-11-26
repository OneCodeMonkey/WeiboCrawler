from tasks.user import crawl_person_infos
from tasks.home import crawl_weibo_datas
import time

# 设计师
uids = [1830893900,1941248741,1719235015,1577580437,1705602977,2993860114,1582733811,3756609632,1738075144,1647162697,1217267701,3062240617,3234940492,2674650822,2505417760,2479574951,2357391917,2031640232,1839481230,1814600347,1690129975,1454159240,1403650930,1296823313,1836608847,6486394291,3240284634,2646334393,2548241730,2079289217,1763416884,1684419644,2933987374,1561500285,1775173777,3823757984,1745181003,1746082445,1646848235,2199825091,5033130895,2721031741,1923999845,2415936504,1612813764,3858152897,2725638965,1344792201,5875020234,5726227568,]

for uid in uids:
    crawl_person_infos(uid)

    crawl_weibo_datas(uid)
    time.sleep(11)


