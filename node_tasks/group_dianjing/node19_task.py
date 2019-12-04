from tasks.user import crawl_person_infos
from tasks.home import crawl_weibo_datas
import time

# 游戏
uids = [1904645824,3480197717,5859571276,1784469760,3972958860,1864197090,2217355702,6589081792,6523485411,6390314930,5718972361,5353688633,5353688625,5353688483,5196870710,3874591519,3565085717,3405840252,3262284735,3164953615,2889078493,2698588482,2483875210,2401266852,2282787833,2165453012,2140885974,2096058301,2044027773,2000534913,1986652563,1977610542,1908276837,1846113022,1830583804,1814982430,1812812614,1811148615,1613280332,1070009427,3200894122,2932880657,2068620751,3247454675,2475419692,6147258984,]

for uid in uids:
    crawl_person_infos(uid)

    crawl_weibo_datas(uid)
    time.sleep(11)


