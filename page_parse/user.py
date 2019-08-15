# -*- coding=UTF-8 -*-
from tasks.workers import app
from page_get import user as user_get
from db.seed_ids import (get_seed_ids, get_seed_by_id, insert_seeds, set_seed_other_crawled)


@app.task(ignore_result = True)
def crawl_follower_fans(uid):
    seed = get_seed_by_id(uid)
    if seed.other_crawled == 0:
        rs = user_get.get_fans_or_followers_ids(uid, 1)
        rs.extend(user_get.get_fans_or_followers_ids(uid, 2))
        datas = set(rs)

        if datas:
            insert_seeds(datas)
        set_seed_other_crawled(uid)


@app.task(ignore_result = True)
def crawl_person_infos(uid):
    if not uid:
        return
    user, is_crawled = user_get.get_profile(uid)
    if user and user.verify_type == 2:
        set_seed_other_crawled(uid)
        return
    if not is_crawled:
        app.send_task('tasks.user.crawl_follower_fans', args=(uid,), queue='fans_followers', routing_key='for_fans_followers')


@app.task(ignore_result = True)
def execute_user_task():
    seeds = get_seed_ids()
    if seeds:
        for seed in seeds:
            app.send_task('tasks.user.crawl_person_infos', args=(seed.uid,), queue='user_crawler', routing_key='for_user_info')
