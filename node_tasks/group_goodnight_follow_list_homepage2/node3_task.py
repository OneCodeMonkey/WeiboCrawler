from tasks.user import crawl_person_infos
from tasks.home import crawl_weibo_datas
import time

# 全部（原创+转发）首页
uids = [6650260660,2978857045,5245145816,7300773128,5202570512,3177609292,5640103194,5646467631,5460712985,5730109622,5316797650,5253880292,5337755243,5326792816,6057303462,5146310717,5404076189,6205878123,6507729109,5712030292,2806113902,6963483588,6505448587,6119745569,5850387375,2070244302,6452395490,1069163945,6122769163,5960537295,5060581531,1851370130,3490710583,5054288122,3554127667,5601440327,6865871853,6226029446,5326045514,1666366107,6457856840,1592249271,6361241377,7224233873,2184452883,5767866061,5470460490,5795225297,6136662269,5904705900,6587965966,2835291055,3448714680,7330763119,2538405583,1786479732,5107588203,5706611407,6604396915,6107955330,7296490303,5274283777,7263777750,3976472053,5603424800,5627146245,5876482893,2871495535,5258402471,5197751787,2943216891,2204079885,5986113320,5836620281,6313767343,5381270942,5236672908,6792680364,5581789352,5774870794,3661225420,2954091475,2437625345,5354921090,6657158863,2012178877,6273181284,7005682976,6509603438,3260981310,1256296210,6395562072,5778319505,1286394042,6035272475,6155594309,5997134418,6575303876,6028211794,7156468646,2514140984,5345890750,5665328985,5466718540,5246107940,6061110988,5898282247,3896506507,6231524219,2269634460,6482841926,6594424346,1766603524,6193230788,1768260735,6043179883,5349789247,2859214190,2497036783,5094972967,5239271213,2855178720,3441587310,5809572522,3004535001,6212529089,5651716460,6232867163,6866153982,5293670668,3886893874,3219223550,6370813985,5662463155,5998987157,5494342586,7342327842,6725992388,6053572857,5960783501,5792708378,6272294506,6804676281,7005106731,6971868596,1956847195,6635198089,5318478227,5367266968,5085219585,6068081158,1626408810,3525962715,5488852064,2362633424,1417913520,3152891714,6295519272,1786623500,3974710930,6637871608,2077823075,6399334770,5290218939,6282296722,5980150075,7320309641,1681443687,6421198156,6288188197,2681602443,6394899821,1809182687,6715589198,6132125238,6481574846,2257898010,5807654281,6034377694,3148017950,6705840763,5056226063,3693389150,5675874879,5519346741,1795824635,6676628416,5833668234,6087708105,6390023976,2682538203,6277304115,5400377402,2245752473,3775167670,3722548365,5028402410,5634098184,5590252311,5086663026,3802726775,2848197113,6431729656,3054363937,3985547181,6276113961,6014876360,6098811940,1749101857,6716527880,5381942292,5273029547,2111120542,3484874420,2656721343,5754328310,2604249920,5481400761,5995156612,5829618744,1734065053,6829586639,5873935894,5915042240,6557023798,6891250160,5503773504,6134668537,6832352071,6035949839,5520035141,6235077560,6271552255,5343798094,3615736425,5223191227,2249602957,3497433814,5495349747,1805913421,7310319515,3133116505,6381553464,6619166634,6568506138,3546336332,6353825567,6486184632,5678703252,3805881812,6742752785,6833066981,5140128108,6441554918,1818498341,5635602780,5124244727,5756068874,6494043714,5837810338,3206238560,2282203493,5064106812,2143773302,6567240754,5692634650,2060473215,5910201377,5747664600,5262587680,7342527733,2063597443,1909377960,7292678220,5812919797,5090723146,5849075008,5748006748,7308270052,6519481133,6919595678,5842593634,2810447215,3558986202,6720947342,6166590061,6938591519,5428692663,6664220295,6302680361,5408360301,5861934508,6067889829,6053885209,1803858371,3098245923,2829961261,2501880784,5977071751,5151170370,6216343399,3308232871,5695979501,7235167967,5857017579,5514431746,2720980721,7283779440,1815982852,2231880333,5360966583,3524179864,5662152389,6416620768,6270813245,5172553041,5893907288,5240346269,2039573263,2535349181,3841042988,5850436338,6335979927,5403501631,6569647114,2185512654,6690720325,2658478847,5938070130,2832908875,2329686957,2497537083,]

for uid in uids:
    crawl_person_infos(uid)

    crawl_weibo_datas(uid)
    time.sleep(3)


