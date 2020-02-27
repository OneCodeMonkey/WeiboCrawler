import sys
import os
o_path = os.getcwd() # 返回当前工作目录
sys.path.append(o_path) # 添加自己指定的搜索路径

from tasks.workers import app
from page_get.user import get_fans_or_followers_ids
from tasks.user import crawl_person_infos


uids = [
2660731545,5055981735,6983840780,3779671480,5686955778,1806752300,2254699702,1861844471,2170800330,3923879175,3214038322,6716182442,1442639384,1040754530,6781615737,3707464664,6333793811,1988134573,2281320287,3928750593,5651671672,6615367445,1863623714,5892365358,6700686040,1761617120,3921841773,2916435885,2857217052,2360570872,2820104280,1945321704,5143341316,2319902810,6528184549,6631079876,7005797130,7030137619,6400475452,6600397259,6550239076,2770971411,6275146334,2269652401,6666772548,5554619675,1777582675,6138198900,6668044941,1998631382,6334730943,1661491844,2155743987,5870255288,6967772457,3896682243,6061635107,7329203609,6137573284,6575901670,3244581404,5500928081,1948269001,6200302810,5171827312,6620764510,6650895737,5474657045,6607353712,5974370437,5231890231,6866530091,2071755383,6819571374,1663140620,5884194569,6308130935,3044623473,6537594513,1656604924,3660932287,3355396712,1715984205,5416745688,2948529901,5735394841,6598534182,6427351227,5372852828,2905646415,5668885350,1653618321,5473751128,1566301073,6023732063,5652644169,2147253081,6052808605,5318520697,5609464568,5225730877,5211427694,5661839246,6869906857,3703913740,5581435739,5028495758,5996044822,2920765494,2014976165,5062658892,3645834824,5408826541,3806568071,6886185630,6078748996,5641252537,3494341305,5312196969,6065400830,5168299086,5188172668,2052978917,5662920228,5059593040,5272724483,5510735090,5887167623,6538363688,7091935576,5585381694,5198496004,3719808284,3169812063,7240718573,5851035933,6629416620,3191817482,5824461532,5843856241,5496090247,5034762164,5790105206,1840529442,3314662181,2515455397,6310437921,6919702085,6291511192,5521663700,6768766122,5052304303,6167698721,7302245522,6196660799,6375594636,1944927414,6602215463,6616164483,6076253054,1847067290,5508520910,1882886573,5994995100,3060183607,6205891817,6781608566,

]

# 爬取关注列表
for uid in uids:
    result = get_fans_or_followers_ids(uid,2,1)
    for user_id in result:
        crawl_person_infos(user_id)
