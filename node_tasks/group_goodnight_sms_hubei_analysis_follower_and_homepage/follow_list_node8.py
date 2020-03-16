import sys
import os
o_path = os.getcwd() # 返回当前工作目录
sys.path.append(o_path) # 添加自己指定的搜索路径

from tasks.workers import app
from page_get.user import get_fans_or_followers_ids
from tasks.user import crawl_person_infos


uids = [
6226504072,1800405225,5682636363,3634469127,7363090278,2867592310,3845005121,1882660622,1844270995,7079851229,1770457812,3990193804,3616527702,5580020155,6752783611,6043501347,6442679667,6812010769,6482902362,6237551842,2613722773,6023563642,1502859012,5671727321,3876115741,7323081824,7269733748,6595188134,6985129418,1674549110,6877721310,5764649400,1877878042,6140070751,6210221047,7017508487,3608448924,6090604200,5857601761,7002043656,5892134806,5551668387,7300300835,1860843253,2415442173,1956986751,5237305332,5299083577,3693264864,1844671634,6816634930,3672462810,3448053222,2162273341,3772695561,5249833369,2927939481,5462336218,1708382174,6207733784,2969161235,2241447702,5508552650,6669325185,6023895181,6070529259,3896919572,5047255418,5933248288,1351146650,6636911773,5124459317,3770200291,1677760602,5338841186,5346465672,2285372805,6041411805,6782995091,6078283980,5747534623,6477439863,1323948544,2766433845,1948085195,5519095633,6083203281,5874313418,6207262987,1818197710,6335853092,6094939394,6799818464,5727222993,7381776665,6752929905,5703003872,1329514894,6980356643,6675894448,1767322851,5710817536,6866722134,2493021595,6997253165,5374760131,5891193792,1945977754,5528479466,1845543387,6256438352,5713048750,6328731935,5637170946,1915387425,2415094832,2659952534,2834915457,5225564533,6513848734,5711477448,2366470455,6165657383,5721493618,7322880622,6117483000,6410261291,6330704203,5914133420,5810636894,6383613313,6664911643,7035597044,7058222692,1805090375,6874861249,1975105155,3176869060,2109635670,6155144562,1806467215,5085669340,1356560710,6148257425,6523042198,6382026183,6936891287,7322231411,2958175380,6858056987,5690927422,5180689926,6542849798,3943139603,6293690111,3501666007,6724825036,6327491210,2521770177,5621847811,1703121305,5733522615,2732594162,6787486183,5134358160,5024951938,3851581543,

]

# 爬取关注列表
for uid in uids:
    result = get_fans_or_followers_ids(uid,2,1)
    for user_id in result:
        crawl_person_infos(user_id)