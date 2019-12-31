from tasks.user import crawl_person_infos
from tasks.home import crawl_weibo_datas
import time

# 全部（原创+转发）首页
uids = [2754050457,1782711787,6333409985,6056610998,6136623452,5795270683,3801757618,2007637227,2126452272,1849609834,1931146820,5991478407,1878436807,6472206211,1785291412,3259170380,1955055371,5833216579,5332661842,2882260812,5545766441,2758761217,3786172991,6913359199,6073704024,5868180598,6134376253,5679094529,6634119225,2727316213,7165046887,7331554381,6411746305,1809983357,2672288463,7219819603,1793859165,5536117655,6148439657,3567850515,3636998942,5647524175,5456320827,1984009513,6115421739,2276164881,5425887138,3185751312,5436330501,5803539985,5854327251,5019353846,2786232417,2813428047,1857007310,1899735087,6561660113,6539801752,2196462102,7285044202,1692115185,2277133774,5260720201,5655327768,6739806667,6523410737,5232594330,5271480883,3650645351,1011695514,7155217171,3269819187,5531805241,3026172853,1965157277,5151413727,1692987565,2673803661,2730356140,3137032825,5815275699,6538436325,6231787524,7285365656,5659977976,5864808732,6362996435,3163476290,3394996894,5462583629,1783389342,3121529953,3153458744,5863783895,5144491057,6795041613,6567300818,5732065092,6246695964,6164979297,6302715603,5637578336,6504711961,1779896635,5801622669,6407724596,3251201942,3784740800,5852630787,6961241284,5401451853,1734246451,5852746610,6306380742,5533315333,5670069693,3921009919,2371870723,6431419047,6623350951,6502758202,5189936629,6398257526,5362851102,6328022727,5519627660,1864657720,6274134224,7322701435,5510852336,6337292741,5843607639,5678514204,2132151704,6863974706,5610946959,6570593663,5673008665,5695971530,2306631680,2694536321,3759000440,1837811232,2689052131,5147822530,6189748347,3681939465,6428736225,5710870941,5615052297,6487461801,6752868115,5841814633,5175006832,5621695009,1877605357,3847937733,2634388527,3772673981,1776080441,5824631912,6030655927,5981968814,1594759315,6171446475,1935977845,6855752250,5747360776,2935349012,5644089606,5652119510,6397879843,5243374253,2771261331,5401477797,2814653611,5541164320,6768622050,5677194033,5619611077,2708296493,5093389886,3235276362,5734178113,3627615522,3947643463,5532766863,5045461985,6942293065,3226313297,1940402457,5385926743,5016415196,3803801075,5528430481,2618615881,5395004756,2713149254,6481613719,6380246513,3523523764,6260067836,2978157482,6084272120,5970584768,5660733365,2924439455,7223239688,5517230060,6601527410,3848068766,6022084694,6375762994,2628687965,5826404743,7174880804,3866398380,5248275399,5283319490,5294652515,5124329542,6192268286,5899209731,2816204334,2765150615,3061099037,2402283433,5023295940,5390282172,3637334940,2362133153,3926532274,5305210602,2305009734,2510306805,6661175946,6486710175,3293767042,5749541689,5153725349,3554725703,5832149788,5723194356,5194580165,5518903022,3614566312,6128320329,6284474822,7104718114,2266995882,5880174162,5822807077,6619173324,5509151587,1843660522,2275688515,3001865767,1949470547,6369218469,2656128853,6083080907,5492022093,5844389311,3281656194,3788186487,6359570699,5658046612,2456089373,6661183071,6094502560,7227034173,5955731207,5611750202,2641232717,6630891903,5713698263,6178714524,5975068045,5683628706,6571334980,6881395567,5239033382,5936250504,6467274380,6325820242,3722455534,2177884364,5680094680,2143968013,5723941896,7265855760,5514816506,6593812998,5267728203,6580669008,1748115011,7327771899,5170386499,5642749464,5666618110,3293426554,3854310715,3022369877,2732634235,2497412752,5683872211,5576309936,3300397562,3313195804,5666206414,5912213552,5869280655,3886611073,6610463303,6368954659,5728811765,1787978147,5576090485,3602804137,5750723463,3853969975,5308376388,3736157535,3789491097,6670680230,3886324086,6880794416,6150297147,5953687788,3392125804,5637574715,5985625165,]

for uid in uids:
    crawl_person_infos(uid)

    crawl_weibo_datas(uid)
    time.sleep(3)

