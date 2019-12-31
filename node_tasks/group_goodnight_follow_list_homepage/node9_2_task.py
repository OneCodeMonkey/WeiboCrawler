from tasks.user import crawl_person_infos
from tasks.home import crawl_weibo_datas
import time

# 全部（原创+转发）首页
uids = [5486080402,5659000642,6348076839,6563364810,6447457109,5746426266,5940620992,2112052592,5198302982,5573148314,3166806565,1665302935,5481854269,6573104585,6460992105,2695096211,6791149279,6227371808,3484644855,5869961189,1782091063,1592080842,5650820467,5525188106,3607682307,5655693036,1978700160,6508774281,7342272207,6091411726,6538072804,3738684557,3800596325,2831995270,5332418533,5393346651,1735006923,6542214401,6351936158,7208652423,3672469353,3191540604,5356250685,7062910520,5935638586,5556114333,6049538586,3104920805,6665218123,6115424567,1840273931,2692568311,6148097703,6293693692,2145076981,2974547673,3516168854,7291652236,5403315665,5830866831,3018838847,3008850995,5680326992,5326753110,6342129473,5859548832,7116396616,3885202612,6853792233,2574776930,6445747796,5572222266,5446968343,5096291050,6200031084,5288727711,5995868982,2474280045,1883555991,6606370566,1719874423,5974121579,6569310994,5184133610,5674069314,1772056384,2485909425,3582862343,2616051133,1460220511,5573327686,6494565109,5415864811,5299534775,2467620692,3581955887,2363292521,5044841000,6034961018,3953539497,6617531538,5964229876,5306140882,2941296511,5272555867,5386698688,2148475924,2336227137,1742359223,5263780517,6521976820,6226925905,2551812565,2667415667,3942543394,2881385862,6070367598,2724141335,3175941650,7350201603,5531516304,6619460211,3719895694,5193607169,6318609636,5728985722,2428393031,5671026960,1863052622,5955768901,5491916875,5113030048,6301597486,1434066280,6538222895,2196932140,5114131785,2000922107,5933860638,3255406173,5882310964,3025589547,2521006031,5816436572,6852628748,1359691391,6448077210,5525663763,5711717950,1800073534,3777366033,3032044573,3300798887,5540760958,6381487904,3271793962,7157947721,6558095521,5648057201,1934392395,5884835134,5457548273,5484585507,7167536413,5853791163,5211789362,5668939078,]

for uid in uids:
    crawl_person_infos(uid)

    crawl_weibo_datas(uid)
    time.sleep(11)

