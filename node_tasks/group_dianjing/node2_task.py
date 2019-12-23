from tasks.user import crawl_person_infos
from tasks.home import crawl_weibo_datas
import time

# 游戏
uids = [3883106777,3882794224,7181234075,3929442634,3922146170,3885412753,3885396646,3883109139,3108476125,3926210450,3885497205,3884988269,3883057197,6452117580,2599602047,3883038022,1692674375,5095933262,3885016303,6445232574,6916853920,6445232384,5872210260,5963800819,5723049611,6995362570,5027208179,7101877694,6512209085,3753923512,5866899501,6637017963,7319714934,3882692382,7000797454,5607039968,1874706794,7293563149,6678995363,6358563086,6060596506,6363057279,6327616597,5865304602,5865302129,5865331894,]

for uid in uids:
    crawl_person_infos(uid)

    crawl_weibo_datas(uid)
    time.sleep(11)

