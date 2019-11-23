from tasks.user import crawl_person_infos
from tasks.home import crawl_weibo_datas
import time

# 游戏
uids = [1801643403,1769862104,1764241425,1567860201,5896513087,1716314577,1713607554,1706926301,6572311455,5370998025,2794252884,1870503497,1770838583,1684166675,2686396281,1772762022,1820338441,1804531244,2611747047,2175931162,1827916372,1852193954,1338099162,1958178973,2285221923,1867939303,2788176594,3256846671,2385056494,1890708734,3202979351,1654591883,2081334623,1794897412,3274052701,5679399630,2558584847,1686576254,3618163381,1859509474,2607990444,6172866479,3434607910,1668692323,2952997041,5112231550,3190740470,6363138583,3159504597,3273716091,3248308760,1807627990,1233357963,2639985723,3466824282,3250783055,2961758583,5742478598,3274560471,1285106533,1644845465,5770145927,5338698416,1706149197,1648575811,1649608047,1912929155,1833203952,2406213380,1649451110,1799244901,5100484058,1758373277,1895264740,2373103393,5601474365,5513176903,1883771101,1151872254,5163181765,3574741877,1883315001,2686415611,3938815337,3289103297,2240875210,6722259311,2150847104,5103621275,2105513227,2459762185,6599419611,1924674903,2106156585,6174481701,3073015713,2425514241,1610915385,1808392133,1250498497,6589290556,3159686244,1804024624,5121964491,2988452332,2092102372,6414242568,5934451102,5072786579,2194098132,1876943407,1655166071,2010916597,1667631617,6261422091,1717851004,6174455936,2703348994,1134046140,1722070410,1280915735,2776554823,1730380283,1728997783,1403366091,5266776347,1649185463,1355323891,1784497824,6590654022,3168577490,3156153911,5455775935,2076854653,1314901714,5657600811,2080710353,1866582284,6431378077,2516156930,6154230089,5637867804,1662223823,1343018293,3016113645,2938214553,5149587726,5121474089,2318693310,1738733270,2513575011,1806194614,5925008909,3514126993,5444651156,5151217211,3597709105,3042973207,2971984814,1935110044,1684347414,2097148762,6238683453,3881495648,3296528114,3123347317,2017225255,1889427247,3205914067,2631981882,5537621849,1818271840,1638736854,1791109745,1777113623,2025374111,6619722100,5647630462,5035167264,3218579804,5589518506,2880231860,2105859182,1904372323,5612068207,5111729936,3435529654,2662534925]

for uid in uids:
    crawl_person_infos(uid)

    crawl_weibo_datas(uid)
    time.sleep(11)


