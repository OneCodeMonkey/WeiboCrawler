from tasks.user import crawl_person_infos
from tasks.home import crawl_weibo_datas
import time

# 全部（原创+转发）首页
uids = [2484804400,6863452789,5925254370,6801342554,6438107579,5883689065,5890128120,3097169871,6046185266,2201072965,6320168822,5661999292,6035290607,1211908295,1951634991,2030749523,1094830133,5557787736,5020496983,3798022400,6327756646,5599726891,2270490230,5842652237,6591476683,5541119595,5881857013,6990301124,3781585510,1807639445,1629477837,7317840592,5604748780,2768703713,5284149020,2707429573,5288436494,3040889351,7284234577,1307561204,1932392350,2653485171,3096033515,6366317797,3730767812,5610850420,1710155317,1876042103,5596478821,3050912901,7019851747,6107573550,5107450190,5579781192,5663132600,5239334869,1954280200,5977870755,3170174230,6007334777,2616892411,5640460917,5237771796,5516961764,6367380180,5784428564,5779211051,6518648942,7346319922,2729088994,2737268520,2750448624,5880320956,6459921640,2837568370,6006631300,2313582702,5102015662,6514136713,1843590353,3060714755,5177300399,5692005018,5271435733,5366711590,6008616101,5584962129,7177224038,3294532252,6006367902,5823083973,5572878553,1875586811,5254027882,1820534602,5491063859,2767891917,1037812971,5905604306,6323281321,1394995161,6676487334,6375795673,5567803534,2611881843,6331336304,1961794941,7013287025,6555830609,7026171437,2829840054,2481205715,1799587731,7313454036,2345425215,2159769664,2354568204,5194390275,5678444841,6297333755,6810254169,2297894163,6044731127,2509679233,2063414981,5593092137,5117723987,5368952632,6193562075,2651069745,5417371391,5539888102,7003384679,6527631515,3040178691,5353237469,5161330624,5828147011,5281631399,2196445561,5583927402,5614341841,7021157071,5307704594,2418891072,5836514747,6635716335,1559458845,1815662971,3630538070,1736443634,5602114509,5092643369,5417573052,2949961230,6445606201,1826270933,7343184289,6285212063,7322496688,2708761265,2787798404,3242539525,6728810110,3258690061,1109769475,6205918858,]

for uid in uids:
    crawl_person_infos(uid)

    crawl_weibo_datas(uid)
    time.sleep(11)


