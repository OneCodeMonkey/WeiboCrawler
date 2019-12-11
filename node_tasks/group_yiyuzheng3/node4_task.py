from tasks.user import crawl_person_infos
from tasks.home import crawl_weibo_datas
import time

# 混合
uids = [1875332097,6496000916,7336943679,5075503635,5698033109,1753071872,3064673167,5599166041,5332043405,1881680874,6074105524,6038354092,5665777122,5370225785,5616125930,6137004325,2734782651,5102707683,3925988616,3848269748,2979386582,3741316952,1809487427,1751727394,3828295068,3205992387,6011150834,6374395022,2279256182,5215220058,1724222727,2746162371,2493710472,1975038237,3153207465,2774735987,2169895381,2604273495,6185106414,6389958272,5491428565,5629802140,2703137480,2173551142,6538761950,5441684145,5512492499,5266781491,7033376297,6122472851,5871953072,3200291613,3645246764,5422362078,2719341377,3803714488,5458514600,6820705802,5623685382,5234025450,5586662034,5498334562,2463794591,2964494493,3228087781,3927952345,5177284816,1756613641,2691808584,2726344277,1244320413,3933781962,1353019367,3785879357,1463318500,1923498714,2613937200,1741672865,2675699351,5740175472,5665541828,2056575587,5650949030,5075890516,5470018861,7074835086,2505008472,5878986373,3683895795,1309359415,3665854273,1700328184,1809681790,2149726102,1844694662,2218655017,6294184264,2148302452,6070531840,3828049678,1858012084,2549838014,1948161323,1789519427,2850912615,6089478396,2393632090,2660858573,1450223910,3427124410,7312309939,1608596560,5846234675,1823112597]

for uid in uids:
    crawl_person_infos(uid)

    crawl_weibo_datas(uid)
    time.sleep(11)
