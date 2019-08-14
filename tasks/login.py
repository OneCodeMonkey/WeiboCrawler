# -*- coding=UTF-8 -*-
import time

from db.redis_db import Cookies
from logger import log
from wblogin import login
from db import login_info
from tasks.workers import app

@app.task(ignore_result = True)
def login_task(name, password):
    login.get_session(name, password)

@app.task(ignore_result = True)
def execute_login_task():
    infos = login_info.get_login_info()
    Cookies.check_login_task()
    log.crawler.info('The login task is starting...')
    for info in infos:
        app.send_task('tasks.login.login_task', args=(info.name, info.password), queue='login_queue', routing_key='for_login')
        time.sleep(10)
