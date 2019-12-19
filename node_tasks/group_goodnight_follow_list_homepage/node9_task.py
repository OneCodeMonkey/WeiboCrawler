from tasks.user import crawl_person_infos
from tasks.home import crawl_weibo_datas
import time

# 全部（原创+转发）首页
uids = [6340939539,5603002671,2162690661,1801705191,1942630675,6902752692,2287763877,5538775592,5456869887,7242769484,5722455068,6458368504,5725685655,1118433324,6391611505,6475170540,2352032204,2261655782,5235413856,6046686817,3645135084,5887548665,6452310917,3934954803,5850872310,6580742229,3211193470,2309817000,6483004439,1701832627,3820934129,5539403725,5925569908,6037920659,5124839482,6648500289,3815806934,7016783960,5773765117,5124715221,2950422433,6575081051,2296141485,2722635184,6389300118,2690192363,5496403574,6018884742,5134937103,6737567744,5462319130,5476099695,1677193463,6134377881,7335862530,5693362459,6053432876,6935394689,1928079753,6486456328,5711811601,6029145945,1623623143,5787011817,5542579563,5656544845,3027860853,5594991459,5064230430,2117467724,6318959482,1245974843,3164813794,2966204320,5181036458,3893531506,5649934507,1692555232,5893179749,3942852723,5596198838,5235437138,5704636805,7032944085,3219327751,5447112508,3977004034,5527101792,5695982824,6508779756,6083873312,6025441693,2393408483,7289366301,5597639886,3938427710,7325421298,2831610283,5224666521,7273804063,5496338075,1582954602,6801370356,5509381204,5332785800,6991752056,1961880773,3896024070,6585088470,6577641134,1661972364,5979572879,6215676345,5247953864,1779171345,5667725690,5855978156,5885874129,5512440036,1837671583,5544913667,7183844598,5980149510,5688273502,3308791497,7334278747,2203798241,7245325193,2583867620,5658003579,5039149641,7303623024,7349878584,6904551587,5635351415,5859674939,5936273015,5854420951,7319649801,1735203183,5528171767,1861231744,1630375212,5982083861,6362782228,2419601040,6067778235,5048164586,3326867552,5677336150,5564393710,2881140300,3602758000,3625537447,5057631300,5936787204,7169658109,6174427187,7292403240,5655312601,5283812475,6280561221,5537132762,5853682062,5673646243,3474014390,5394704242,5486080402,5659000642,6348076839,6563364810,6447457109,5746426266,5940620992,2112052592,5198302982,5573148314,3166806565,1665302935,5481854269,6573104585,6460992105,2695096211,6791149279,6227371808,3484644855,5869961189,1782091063,1592080842,5650820467,5525188106,3607682307,5655693036,1978700160,6508774281,7342272207,6091411726,6538072804,3738684557,3800596325,2831995270,5332418533,5393346651,1735006923,6542214401,6351936158,7208652423,3672469353,3191540604,5356250685,7062910520,5935638586,5556114333,6049538586,3104920805,6665218123,6115424567,1840273931,2692568311,6148097703,6293693692,2145076981,2974547673,3516168854,7291652236,5403315665,5830866831,3018838847,3008850995,5680326992,5326753110,6342129473,5859548832,7116396616,3885202612,6853792233,2574776930,6445747796,5572222266,5446968343,5096291050,6200031084,5288727711,5995868982,2474280045,1883555991,6606370566,1719874423,5974121579,6569310994,5184133610,5674069314,1772056384,2485909425,3582862343,2616051133,1460220511,5573327686,6494565109,5415864811,5299534775,2467620692,3581955887,2363292521,5044841000,6034961018,3953539497,6617531538,5964229876,5306140882,2941296511,5272555867,5386698688,2148475924,2336227137,1742359223,5263780517,6521976820,6226925905,2551812565,2667415667,3942543394,2881385862,6070367598,2724141335,3175941650,7350201603,5531516304,6619460211,3719895694,5193607169,6318609636,5728985722,2428393031,5671026960,1863052622,5955768901,5491916875,5113030048,6301597486,1434066280,6538222895,2196932140,5114131785,2000922107,5933860638,3255406173,5882310964,3025589547,2521006031,5816436572,6852628748,1359691391,6448077210,5525663763,5711717950,1800073534,3777366033,3032044573,3300798887,5540760958,6381487904,3271793962,7157947721,6558095521,5648057201,1934392395,5884835134,5457548273,5484585507,7167536413,5853791163,5211789362,5668939078,5110467855,6295765231,6029730703,5650845190,3302761975,2157230107,2859742872,5292294508,1100712514,5894173831,2313649623,5044180969,2769327443,5421521091,5677814380,2574842797,3737022715,6354382298,3309136545,3887763871,5254982468,6182815768,6682199870,5312593053,6648678855,7160717448,6477696381,6006103225,5088983434,5579634050,5629466676,5999184016,2729064724,5562688933,6456965011,6336188411,5107111519,5905674981,3852457882,3232176532,5581857280,7144888662,2522174694,6087539339,2011349610,2703507462,1629261317,3250206874,2601078937,2650326402,3123995751,5094749681,5890796321,6486847419,5098648291,2812961701,3121410563,5994747421,2936987455,3934916865,6985749629,5255147358,6364002896,6616857121,3069880515,3574526334,2759981261,5725868837,5723745502,5707176487,5029544863,6580023674,5655971606,7350169789,5197399791,3807198851,6502322103,5175652901,5879511240,3846427898,5949615115,2142562080,2137142714,6971860473,6457290214,7269549722,6383627429,5792466345,1794147052,7314316505,5180315032,2419098950,6474356622,5802668286,5446434618,5520013338,6335587736,5978199036,5516516086,7347526420,5867745784,6895849307,5304706612,5820829916,2104651874,2658848063,3232352505,5226505748,1941152505,5414473517,2447723614,6245970852,6015036035,5469632154,5566373203,6504937431,3849422383,5660378178,2949121532,2607167911,5578307704,6520887487,5204828012,5609767848,6296175097,5228968979,2254514533,2932770294,6921891108,1216692333,5760558739,5031102576,5031043989,1967109401,2970449297,6619164924,5668111469,5776493871,1040013913,5628117014,7324612211,5913735771,5620172046,7307452520,6513987102,6294543285,2360685622,2724718930,7282724488,1906694804,1857482221,2881725930,3185396154,5649948458,1783878050,7315653962,1681812964,3210821302,5523957955,2870740501,5597601571,1838672284,7071470782,5538635956,2960256963,1758921870,]

for uid in uids:
    crawl_person_infos(uid)

    crawl_weibo_datas(uid)
    time.sleep(11)


