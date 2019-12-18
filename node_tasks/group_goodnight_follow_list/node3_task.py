from tasks.workers import app
from page_get.user import get_fans_or_followers_ids
from tasks.user import crawl_person_infos


uids = [3626591085,5121746417,5243345718,7346733107,5673728454,5450600864,5997499853,3967506449,5767717228,5636206539,6177551833,3225226130,5700847887,2839528574,2233236401,5399907988,6239503465,2642732727,5187925801,5323391489,5970495834,5015838093,5202768579,5854459674,5107528888,5706341127,2594183077,5499640823,3247302314,5667800990,3015292555,1733486310,7295868332,5413893049,3204841213,2379591747,5645448334,7267699339,3820702061,5427135074,1889784197,6006198439,6613988969,6914571121,5878776721,5106463234,1751758165,3822385587,5880885157,7349813264,5518926493,5253461990,5507896881,3139992332,5640711699,5123307570,5998069518,6671033976,1887649745,5012526449,3200692720,7194306977,3736140910,5146142646,6569929470,5627065401,2172518072,2032411923,7202325283,5537697080,6223924110,6164950244,2547452341,3656594147,6134430274,5653429163,5953282231,2812561384,7037410480,5255712368,5612984410,5893831697,1869143947,1837710497,7059947410,5252749928,5860171463,5986487921,6570912637,3930749726,7211716968,2856830455,5389745011,6669124219,5974718874,6129831768,6208287183,5657451265,5144936452,6235614466,5235953715,6062190702,6676107329,6451966675,1950100111,5539405414,3780673123,2165812573,2796361864,3727277940,5936179502,6033696671,3837481838,7349859747,2516191604,6013925646,5832640055,7204130737,5878917849,5533081040,6035294329,6581020133,5635633371,3836886522,3277158390,5802509113,7128392311,5822759368,3877425593,5888894116,3962782269,5261868680,7093565306,7124519954,6513390814,3264146502,1703473130,6966659973,7324066984,6218116239,1832442950,6530941894,2465515044,5629142201,5090739921,5362377862,5609340389,5370080001,2027954110,3046682631,6573507645,2434852294,5664160054,6911925786,5961161375,2575928767,5091749144,5538605695,7002305011,5671489568,1765816650,5391626504,2282821372,2669377665,5909927582,5636172763,5921880809,6474007419,3764367384,6519218892,5872544302,2543689853,2695052282,7042144074,5863306650,6025395611,5767269833,2852483213,7085412781,5742999065,5599662110,1944252981,5894078599,7244083787,5203167943,2698039101,5808317150,5124837934,7009740014,1046205062,7204704867,1807608422,3548449221,3785678844,6495775010,6187529898,5782493091,6830838976,6331692425,5477252319,5663899326,6283074991,5188592900,2635810571,5945563433,1849980671,6293378444,5494048660,6276869191,6527954839,5341953021,6166104171,2386563244,5341741600,3779585980,2720784673,1504548987,3220123254,7097174707,6542801805,6474630125,5590956018,5507713641,6064027646,3970054277,5949803741,5951340850,5998042521,6157240343,3206932147,5321801762,6401188508,3034651711,5605350718,5403468196,5633977559,5600112952,6000096176,5448453870,2435121522,6696073657,1501593440,2549910107,3024741005,7349856994,6269731419,6556178609,1657858304,6677169420,5213778621,1970942697,5679661144,6036490575,3801954539,5217481453,6587142758,5470056938,2677854747,6378413160,6031765743,3994486139,6660668113,2022623163,5219282231,6589327575,2134263451,6141684958,3926476611,3704979920,6054337328,6121865295,3354776622,3910743140,5337468709,6369528271,5871171417,7328521385,6683286253,6610207121,5910779731,5044988090,2847608921,6232202472,5531274979,5097364193,5948386213,6481370502,6014733169,5669101562,5211705608,5292393120,5845017216,7303418031,3887211946,6025429868,5261473204,5993435172,3622711543,5321488703,3559084855,7336123352,6507760648,6871933092,5881703876,5700001333,3686934467,2653446444,1926161307,5856378126,5233871196,3937646009,1609850425,6355861735,6223563627,5040134947,5127458002,3819101748,1969068051,2393664622,1934771115,1827886890,5197886192,6364027753,5831354643,5743015031,2247606345,3823612657,6866665770,6580966469,6402663341,5247640489,1959190607,5441849963,5891812874,3080998081,5901205982,1987747987,3335214460,5473378364,5576167242,2803483881,3545059114,5516370930,7134977903,5252577187,1108665921,6519114679,6270188111,2020952061,6937286939,5253524468,5869314408,2692946122,6595365626,5457721156,3607721540,5292642502,5066543177,5713695845,5702218106,5711579173,3889891096,1680243167,6204048594,6170905164,6299621515,1491607165,3783122363,5257495146,5494324454,5269681002,6594961301,5451856696,5632158717,6069053571,5224629963,7138010077,5539916154,1782312494,2120562832,5672075323,1110495162,5635355578,5195491587,1640656683,5452040579,5579499742,5682236724,5949281195,6570421415,6450957014,5288904381,2594581235,3645194953,1851355712,6376970045,3224178630,2061709691,1794160904,6085663830,2768737615,2020674453,3989894265,2492080043,7186128096,2907993521,3942255569,3784279032,7187919997,6028244472,1756569025,2692671360,6366326214,6585266041,6640582506,2529578860,2886329412,3490093712,6449299326,3120689805,3163843891,3182720891,6169818047,6551545158,6280661695,5601605314,5238341828,1882521733,5632755816,1868134241,5261649648,3936966150,6774009831,1358240974,5897908399,6300208282,6110311549,2780072531,1987357031,5748119122,5633887033,1143700814,6128952408,6060501144,6534517909,1763019331,2652820885,2119848645,7107260834,5293032425,2890803237,2675147554,6439036251,5188108121,5350279541,6617607257,5406393891,7350207786,5399148331,5379142075,3250588805,1767389022,3854395114,6574171908,5946091785,5985507593,5242681420,1918399611,5189984981,5589932900,5352235453,3854626586,5985242650,5885859162,3118685625,1821197465,6129321989,2560810654,2186059507,1884468364,3193958512,5988159795,5092494448,5322792092,5717601461,1620541514,3234099124,5882316606,6729192869,6033425466,1796725777,1768106657,1938703654,1778442027,5947082798,2817499453,3305672213,6022208012,6483087651,7115574795,5320842788,2463128932,3809734924,5126387801,2949327967,3939609031,5233181589,3824913615,5671238347,5344437075,3723371905,6277151772,5503104837,5285834692,2701404307,1849613645,6006441869,5335822966,3580000600,6414765687,2247125945,2875570797,1959303941,6279344670,3524157260,5394202922,6064514133,6619990836,7325814913,2557063972,6857725900,3488776964,3281944654,3944098835,2694865111,2410779121,3305294402,1935593231,6125708725,5904056028,7219336114,3502211020,1644030471,5785226690,1749947714,6067717236,5561285724,5664158635,3455085014,5307842388,5869611881,5972070349,6891245002,1838193621,6291072711,5426416447,6502198074,5745371610,1626900280,5736424807,5619228270,6156772857,2633410247,5898282942,5766709802,6719292287,5775240093,3075827051,5890504736,3081328923,3797870680,5952944232,3977540827,5853928380,6367576476,3993814895,1671390890,5090456811,2303661295,1828088620,5536247798,2136464537,5720618032,6047470670,2554450992,1943984644,5261677726,6112610992,7200468912,7048505716,5477632489,5336145996,3859920466,1789601307,5990977040,7328445742,7349887600,5274980858,3176857181,5411027038,3639637543,6598815890,6138408782,3975595546,2801785577,2828531384,5217004144,5978606916,5184851324,5538102250,7200872728,5635403440,2217366275,3904592678,2813458767,6283028842,6026767351,3570432021,6024312711,5852405249,1833923373,6572453448,2012720902,5984173015,6354380937,5361895665,6879610075,6506991864,1979882757,3300499851,5635617149,5940831567,5948747487,5504916614,1865384995,6784343734,2144399012,6539734865,6585529400,5239470984,7281512755,5664773625,5384228461,3291117175,6205110002,6366999327,3283729015,5860176636,5616130242,1923459004,2960895977,7335654198,5824495048,5551432828,2925362791,7211708669,6178455951,1420104554,6459957468,6902797925,2382006675,6122486707,6993806976,6340939539,5603002671,2162690661,1801705191,1942630675,6902752692,2287763877,5538775592,5456869887,7242769484,5722455068,6458368504,5725685655,1118433324,6391611505,6475170540,2352032204,2261655782,5235413856,6046686817,3645135084,5887548665,6452310917,3934954803,5850872310,6580742229,3211193470,2309817000,6483004439,1701832627,3820934129,5539403725,5925569908,6037920659,5124839482,6648500289,3815806934,7016783960,5773765117,5124715221,2950422433,6575081051,2296141485,2722635184,6389300118,2690192363,5496403574,6018884742,5134937103,6737567744,5462319130,5476099695,1677193463,6134377881,7335862530,5693362459,6053432876,6935394689,1928079753,6486456328,5711811601,6029145945,1623623143,5787011817,5542579563,5656544845,3027860853,5594991459,5064230430,2117467724,6318959482,1245974843,3164813794,2966204320,5181036458,3893531506,5649934507,1692555232,5893179749,3942852723,5596198838,5235437138,5704636805,7032944085,3219327751,5447112508,3977004034,5527101792,5695982824,6508779756,6083873312,6025441693,2393408483,7289366301,5597639886,3938427710,7325421298,2831610283,5224666521,7273804063,5496338075,1582954602,6801370356,5509381204,5332785800,6991752056,1961880773,3896024070,6585088470,6577641134,1661972364,5979572879,6215676345,5247953864,1779171345,5667725690,5855978156,5885874129,5512440036,1837671583,5544913667,7183844598,5980149510,5688273502,3308791497,7334278747,2203798241,7245325193,2583867620,5658003579,5039149641,7303623024,7349878584,6904551587,5635351415,5859674939,5936273015,5854420951,7319649801,1735203183,5528171767,1861231744,1630375212,5982083861,6362782228,2419601040,6067778235,5048164586,3326867552,5677336150,5564393710,2881140300,3602758000,3625537447,5057631300,5936787204,7169658109,6174427187,7292403240,5655312601,5283812475,6280561221,5537132762,5853682062,5673646243,3474014390,5394704242,5486080402,5659000642,6348076839,6563364810,6447457109,5746426266,5940620992,2112052592,5198302982,5573148314,3166806565,1665302935,5481854269,6573104585,6460992105,2695096211,6791149279,6227371808,3484644855,5869961189,1782091063,1592080842,5650820467,5525188106,3607682307,5655693036,1978700160,6508774281,7342272207,6091411726,6538072804,3738684557,3800596325,2831995270,5332418533,5393346651,1735006923,6542214401,6351936158,7208652423,3672469353,3191540604,5356250685,7062910520,5935638586,5556114333,6049538586,3104920805,6665218123,6115424567,1840273931,2692568311,6148097703,6293693692,2145076981,2974547673,3516168854,7291652236,5403315665,5830866831,3018838847,3008850995,5680326992,5326753110,6342129473,5859548832,7116396616,3885202612,6853792233,2574776930,6445747796,5572222266,5446968343,5096291050,6200031084,5288727711,5995868982,2474280045,1883555991,6606370566,1719874423,5974121579,6569310994,5184133610,5674069314,1772056384,2485909425,3582862343,2616051133,1460220511,5573327686,6494565109,5415864811,5299534775,2467620692,3581955887,2363292521,5044841000,6034961018,3953539497,6617531538,5964229876,5306140882,2941296511,5272555867,5386698688,2148475924,2336227137,1742359223,5263780517,6521976820,6226925905,2551812565,2667415667,3942543394,2881385862,6070367598,2724141335,3175941650,7350201603,5531516304,6619460211,3719895694,5193607169,6318609636,5728985722,2428393031,5671026960,1863052622,5955768901,5491916875,5113030048,6301597486,1434066280,6538222895,2196932140,5114131785,2000922107,5933860638,3255406173,5882310964,3025589547,2521006031,5816436572,6852628748,1359691391,6448077210,5525663763,5711717950,1800073534,3777366033,3032044573,3300798887,5540760958,6381487904,3271793962,7157947721,6558095521,5648057201,1934392395,5884835134,5457548273,5484585507,7167536413,5853791163,5211789362,5668939078,5110467855,6295765231,6029730703,5650845190,3302761975,2157230107,2859742872,5292294508,1100712514,5894173831,2313649623,5044180969,2769327443,5421521091,5677814380,2574842797,3737022715,6354382298,3309136545,3887763871,5254982468,6182815768,6682199870,5312593053,6648678855,7160717448,6477696381,6006103225,5088983434,5579634050,5629466676,5999184016,2729064724,5562688933,6456965011,6336188411,5107111519,5905674981,3852457882,3232176532,5581857280,7144888662,2522174694,6087539339,2011349610,2703507462,1629261317,3250206874,2601078937,2650326402,3123995751,5094749681,5890796321,6486847419,5098648291,2812961701,3121410563,5994747421,2936987455,3934916865,6985749629,5255147358,6364002896,6616857121,3069880515,3574526334,2759981261,5725868837,5723745502,5707176487,5029544863,6580023674,5655971606,7350169789,5197399791,3807198851,6502322103,5175652901,5879511240,3846427898,5949615115,2142562080,2137142714,6971860473,6457290214,7269549722,6383627429,5792466345,1794147052,7314316505,5180315032,2419098950,6474356622,5802668286,5446434618,5520013338,6335587736,5978199036,5516516086,7347526420,5867745784,6895849307,5304706612,5820829916,2104651874,2658848063,3232352505,5226505748,1941152505,5414473517,2447723614,6245970852,6015036035,5469632154,5566373203,6504937431,3849422383,5660378178,2949121532,2607167911,5578307704,6520887487,5204828012,5609767848,6296175097,5228968979,2254514533,2932770294,6921891108,1216692333,5760558739,5031102576,5031043989,1967109401,2970449297,6619164924,5668111469,5776493871,1040013913,5628117014,7324612211,5913735771,5620172046,7307452520,6513987102,6294543285,2360685622,2724718930,7282724488,1906694804,1857482221,2881725930,3185396154,5649948458,1783878050,7315653962,1681812964,3210821302,5523957955,2870740501,5597601571,1838672284,7071470782,5538635956,2960256963,1758921870,2484804400,6863452789,5925254370,6801342554,6438107579,5883689065,5890128120,3097169871,6046185266,2201072965,6320168822,5661999292,6035290607,1211908295,1951634991,2030749523,1094830133,5557787736,5020496983,3798022400,6327756646,5599726891,2270490230,5842652237,6591476683,5541119595,5881857013,6990301124,3781585510,1807639445,1629477837,7317840592,5604748780,2768703713,5284149020,2707429573,5288436494,3040889351,7284234577,1307561204,1932392350,2653485171,3096033515,6366317797,3730767812,5610850420,1710155317,1876042103,5596478821,3050912901,7019851747,6107573550,5107450190,5579781192,5663132600,5239334869,1954280200,5977870755,3170174230,6007334777,2616892411,5640460917,5237771796,5516961764,6367380180,5784428564,5779211051,6518648942,7346319922,2729088994,2737268520,2750448624,5880320956,6459921640,2837568370,6006631300,2313582702,5102015662,6514136713,1843590353,3060714755,5177300399,5692005018,5271435733,5366711590,6008616101,5584962129,7177224038,3294532252,6006367902,5823083973,5572878553,1875586811,5254027882,1820534602,5491063859,2767891917,1037812971,5905604306,6323281321,1394995161,6676487334,6375795673,5567803534,2611881843,6331336304,1961794941,7013287025,6555830609,7026171437,2829840054,2481205715,1799587731,7313454036,2345425215,2159769664,2354568204,5194390275,5678444841,6297333755,6810254169,2297894163,6044731127,2509679233,2063414981,5593092137,5117723987,5368952632,6193562075,2651069745,5417371391,5539888102,7003384679,6527631515,3040178691,5353237469,5161330624,5828147011,5281631399,2196445561,5583927402,5614341841,7021157071,5307704594,2418891072,5836514747,6635716335,1559458845,1815662971,3630538070,1736443634,5602114509,5092643369,5417573052,2949961230,6445606201,1826270933,7343184289,6285212063,7322496688,2708761265,2787798404,3242539525,6728810110,3258690061,1109769475,6205918858,5356549085,5744234654,1795427301,7219512976,6714512152,7267188915,6586871928,3123229193,5834833511,3844946600,5786495653,3826709629,2254932217,7148866153,5332913929,5246725661,5991588898,1909526381,6091822836,7342284569,3028039530,2451073952,1679890917,7266887804,2388163457,5485582986,5777746334,5035549647,2270400453,6152723760,5081092859,5878866615,5493532241,5836067356,2276822027,6224208762,5578833725,2015388317,5880265795,1761924317,6700802602,5392691436,5167663737,5659598855,5190213047,7089118185,6418898025,5268301934,5684090328,7324746417,1801589582,7274406052,3287571551,5749046620,1762930744,5975415482,3319214701,6324564527,6612993577,6049330465,6157519667,1767271357,5166813240,5538517518,1800179815,5856598757,6484297767,2871786360,2879577972,5448645689,7308697666,5991641431,7350200146,6542721756,5884458206,5938914564,5164462296,2966304574,1945975105,3206434771,2021623955,6051432704,1783759274,2411404704,5545743520,5590115179,5403797642,5718119276,5669478936,1946795564,2696113045,2181108444,6806255162,6571702482,1114821317,5165605670,1739253852,3265055183,1923141927,5848947667,5467249299,3646108665,5881941030,5080206129,5462634189,5144964222,1984008991,5336033227,7340431911,5072514500,3191800493,6176347748,6240911628,5511621809,5947329035,5797620646,6286356944,6426297075,6788717804,1971748213,1607312251,5830180041,6415881338,5946131777,1341815243,1725410903,2936970635,3219658041,1267581714,6331711112,5656764212,5015509052,6375605935,2278594617,3290093430,6650102607,6611669179,5961023530,5986275849,5364560202,6074016243,1892090674,5337306127,1637420184,7279350798,5268024358,5090265623,2854473850,1840132302,6735519049,5224596655,6609480237,2879204782,3305433492,6436304942,5817672362,5650744750,5519637431,6337649372,5368121100,3679757362,1788468297,5284411301,1926678822,7305590508,6120941397,5509908188,5184480956,6579641050,1883164413,2163253587,3153385683,6468796462,3313790304,3285720000,5121026914,2613262635,1885403503,6154698792,6869528361,2023703505,6941371151,6515011399,5856621917,6032302264,5976343442,6631014037,6005386829,2143755205,3888271080,6028287356,1946860652,6454351068,3763771957,5323908400,3971912255,2006391125,1801306307,6222454637,6331459466,5653862892,2760162397,3179208877,1582337787,5894089811,2422151692,5281049069,2712315413,5876235658,6432599056,1896348591,1696847712,6042556606,5628292460,2122024160,5412991671,2292584961,5717093931,6224147339,5699584523,2603034761,5894521709,5417582228,2036086075,5241570512,3250638882,6263949173,6602138209,7335867961,6938434318,2487636371,2610576641,6494565748,2279721027,5842341268,5664472284,2035763687,5494183593,6410843861,3235294590,7186790303,5171518663,2973991851,1909329373,6109469283,3731274192,6966578071,6375054376,6586164198,5802059597,5672733669,5301311531,3841978835,5261342481,5849231887,5773927246,5866189239,3026893461,2956697281,2446722651,5269909307,5350509769,5964184998,1587683054,5451151879,7263543938,7344963227,5848878240,5590107787,5574218121,6323277261,2585684362,1834981397,5504570360,1491517290,6975191894,5064375810,6732533891,6260397548,3192529900,6314638207,3133474942,2110383533,7209436274,7317975646,1746726507,5123753109,2828967855,2629310203,5953540833,2945586323,5127252501,5492394169,5715886731,5976471935,5537781198,5846079963,5659527659,2782254085,3846000436,5832754487,2421240742,6674787666,6065400830,5310652650,7141120588,3973535862,5604229047,6610863848,6469984042,5976718130,2294871555,3696218172,6094288210,2019863157,1790686143,5224168340,5298018715,6030732189,6393831085,5222841316,5668028635,3932965059,2160257191,6473355458,5658295841,5098354132,2044263792,3870787200,1834470467,3883258299,5310158008,6468648963]

# 爬取关注列表
for uid in uids:
    result = get_fans_or_followers_ids(uid,2,1)
    for user_id in result:
        crawl_person_infos(user_id)
