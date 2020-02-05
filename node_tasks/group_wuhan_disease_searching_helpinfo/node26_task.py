import sys
import os
o_path = os.getcwd() # 返回当前工作目录
sys.path.append(o_path) # 添加自己指定的搜索路径

from logger import crawler
from tasks.workers import app
from tasks.search import search_keyword

KEYWORDS = [
    "湖北 社区 疫情",
    "武汉 感动",
    "金银潭医院 肺炎",
    "武汉封城",
    "金银潭医院 痊愈",
    "武汉 痊愈",
    "武汉 疫区",
    "武汉 疫情",
    "湖北 孕妇",
    "孕妇 新型冠状病毒",
    "黄石 物资",
    "黄石 疫情",
    "武汉 住院",
    "武汉 疫情",
    "爸爸 医院",
    "妈妈 医院",
    "武汉 肺炎",
    "肺炎 求助",
    "武汉 求助",
    "黄冈 求助",
    "黄冈 肺炎",
    "孝感 肺炎",
    "孝感 求助",
    "湖北 肺炎",
    "湖北 求助",
    "肺炎患者求助",
    "肺炎 住院",
    "求助 住院",
    "疫情",
    "疫区",
    "肺炎 确诊",
    "肺炎",
    "确诊",
    "金银潭医院",
    "火神山",
    "雷神山",
    "一线",
    "医护人员",
    "疫区 志愿者",
    "捐赠 物资",
    "疑似病例",
    "发烧咳嗽",
    "隔离",
    "重症",
    "湖北 一线 疫情",
    "湖北 肺炎 确诊",
    "湖北 疫区",
    "湖北 住院",
    "湖北 口罩 防护服",
    "湖北 医生 护士",
    "湖北 医院",
    "湖北 物资",
    "湖北 捐赠",
    "湖北 出不了门",
    "湖北 爆发",
    "湖北 疑似病例",
    "武汉 疑似",
    "武汉 孕妇 新型冠状病毒",
    "武汉 隔离",
    "武汉 轻症",
    "武汉 重症",
    "武汉 温暖",
]

while 1:
    for KEYWORD in KEYWORDS:
        crawler.info("sending searching task with keyword:" + str(KEYWORD))
        search_keyword(KEYWORD, 1)