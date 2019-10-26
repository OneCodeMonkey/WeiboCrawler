# -*- coding=UTF-8 -*-
import requests
import time
import datetime
from logger import crawler

topics = ["#大学的人脉重要不重要#", "#珍惜愿意为你拎包的男生#", "#校园欺凌有多可怕#", "#当我说出永远爱你的时候#", "#你看过最上头的剧#", "#单身久了的特征#", "#情感语录#", "#家的模样#", "#和对象第一次接吻的经历#", "#女生可以爱到多卑微#", "#一句话形容你的大学生活#", "#大学异地恋是什么感觉#", "#年轻人先攒钱还是先生活#", "#该不该跟环卫工人说谢谢#", "#表白时的仪式感有多重要#", "#情侣间的消费该不该AA制#", "#大学多少生活费适合#", "#父母眼里的奇葩职业#", "#青少年心理教育的重要性#", "#分手后能不能和前任做朋友#", "#结婚应该门当户对吗#", "#头像#", "#明天会更好#", "#谈恋爱最忌讳的是什么#", "#男生怎样才算很爱一个女生#", "#大学生兼职是好事吗#", "#让一个成年人崩溃有多简单#", "#闺蜜头像#", "#美女#", "#你见过最阴暗的事是什么#", "#如何看待学校各项规定#", "#离异再婚为什么那么难#", "#男生最让人反感的行为是什么#", "#异地恋分手前的三大征兆#", "#如何看待假装抢着买单#", "#被对象逼婚该不该妥协#", "#不发朋友圈只发微博的原因#", "#酷酷说早安#", "#婚礼现场最感动的瞬间是什么#", "#越努力越幸运#", "#让你幸福感爆棚的瞬间#", "#爱情#", "#十七岁做过最美好的事#", "#老公出轨该不该借钱离婚#", "情侣间最理想的相处方式#", "#智慧语录#", "#早安心语#", "#至今不敢告诉父母的一件事#", "#早鸟分享#", "#夫妻相#", "#90后的中年危机有多恐怖#", "#前任回头草该不该吃#", "#恋爱中的男人可以多幼稚#", "#女友说的那些话不能信#", "#如何看待未成年人犯罪#", "#这辈子嚼过最难忘的东西#", "#女生喜欢上一个人的征兆#", "#异地恋分手还会接受异地吗#", "#夫妻关系#", "#单身而且毫无暧昧对象#"]

for topic in topics:
    STARTTIME = '2019-10-22 11:00:00'
    ENDTIME = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    KEYWORD = topic

    start_time = datetime.datetime.strptime(STARTTIME, "%Y-%m-%d %H:%M:%S")
    end_time = datetime.datetime.strptime(ENDTIME, "%Y-%m-%d %H:%M:%S")

    OneHour = datetime.timedelta(hours=1)

    time1 = start_time
    time2 = start_time + OneHour


    def get_topic_data(keyword, start_time='', end_time=''):
        from tasks.topic import search_keyword_topic
        search_keyword_topic(keyword, 33, start_time, end_time)


    while 1:
        while time1 < end_time:
            start_time_str = time1.strftime("%Y-%m-%d-%H")
            end_time_str = time2.strftime("%Y-%m-%d-%H")
            print(start_time_str, '--', end_time_str)

            crawler.info("we are crawling keyword:{}, timerange {}:{} content" . format(KEYWORD, start_time_str, end_time_str))
            get_topic_data(KEYWORD, start_time_str, end_time_str)
            time1 = time1 + OneHour
            time2 = time2 + OneHour

        time1 = start_time
        time2 = start_time + OneHour
        end_time = datetime.datetime.strptime(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())), "%Y-%m-%d %H:%M:%S")
