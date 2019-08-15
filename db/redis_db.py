# -*- coding=UTF-8 -*-
import json,socket,datetime,redis
from redis.sentinel import Sentinel
from logger.log import crawler
from config.conf import (get_redis_args,get_share_host_count,get_running_mode,get_cookie_expire_time)


mode = get_running_mode()
share_host_count = get_share_host_count()

redis_args = get_redis_args()
password = redis_args.get('password', '')
cookies_db = redis_args.get('cookies', 1)
urls_db = redis_args.get('urls', 2)
broker_db = redis_args.get('broker', 5)
backend_db = redis_args.get('backend', 6)
id_name_db = redis_args.get('id_name', 8)
cookie_expire_time = get_cookie_expire_time()
data_expire_time = redis_args.get('expire_time') * 60 * 60

sentinel_args = redis_args.get('sentinel', '')

if sentinel_args:
    master_name = redis_args.get('master')
    socket_timeout = int(redis_args.get('socket_timeout', 2))
    sentinel = Sentinel([(args['host'], args['port']) for args in sentinel_args], password=password, socket_timeout=socket_timeout)
    cookies_con = sentinel.master_for(master_name, socket_timeout=socket_timeout, db=cookies_db)
    broker_con = sentinel.master_for(master_name, socket_timeout=socket_timeout, db=broker_db)
    urls_con = sentinel.master_for(master_name, socket_timeout=socket_timeout, db=urls_db)
    id_name_db = sentinel.master_for(master_name, socket_timeout=socket_timeout, db=id_name_db)
else:
    host = redis_args.get('host', '127.0.0.1')
    port = redis_args.get('port', 6379)
    cookies_con = redis.Redis(host=host,port=port,password=password,db=cookies_db)
    broker_con = redis.Redis()