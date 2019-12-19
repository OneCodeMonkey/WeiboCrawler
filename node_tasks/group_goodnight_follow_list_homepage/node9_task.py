from tasks.user import crawl_person_infos
from tasks.home import crawl_weibo_datas
import time

# 全部（原创+转发）首页
uids = [6340939539,5603002671,2162690661,1801705191,1942630675,6902752692,2287763877,5538775592,5456869887,7242769484,5722455068,6458368504,5725685655,1118433324,6391611505,6475170540,2352032204,2261655782,5235413856,6046686817,3645135084,5887548665,6452310917,3934954803,5850872310,6580742229,3211193470,2309817000,6483004439,1701832627,3820934129,5539403725,5925569908,6037920659,5124839482,6648500289,3815806934,7016783960,5773765117,5124715221,2950422433,6575081051,2296141485,2722635184,6389300118,2690192363,5496403574,6018884742,5134937103,6737567744,5462319130,5476099695,1677193463,6134377881,7335862530,5693362459,6053432876,6935394689,1928079753,6486456328,5711811601,6029145945,1623623143,5787011817,5542579563,5656544845,3027860853,5594991459,5064230430,2117467724,6318959482,1245974843,3164813794,2966204320,5181036458,3893531506,5649934507,1692555232,5893179749,3942852723,5596198838,5235437138,5704636805,7032944085,3219327751,5447112508,3977004034,5527101792,5695982824,6508779756,6083873312,6025441693,2393408483,7289366301,5597639886,3938427710,7325421298,2831610283,5224666521,7273804063,5496338075,1582954602,6801370356,5509381204,5332785800,6991752056,1961880773,3896024070,6585088470,6577641134,1661972364,5979572879,6215676345,5247953864,1779171345,5667725690,5855978156,5885874129,5512440036,1837671583,5544913667,7183844598,5980149510,5688273502,3308791497,7334278747,2203798241,7245325193,2583867620,5658003579,5039149641,7303623024,7349878584,6904551587,5635351415,5859674939,5936273015,5854420951,7319649801,1735203183,5528171767,1861231744,1630375212,5982083861,6362782228,2419601040,6067778235,5048164586,3326867552,5677336150,5564393710,2881140300,3602758000,3625537447,5057631300,5936787204,7169658109,6174427187,7292403240,5655312601,5283812475,6280561221,5537132762,5853682062,5673646243,3474014390,5394704242,]

for uid in uids:
    crawl_person_infos(uid)

    crawl_weibo_datas(uid)
    time.sleep(11)


