# -*- coding=UTF-8 -*-
import os,time,signal,requests
from headers import headers
from db.redis_db import Urls
from db.redis_db import Cookies
from logger.log import crawler,other
from db.login_info import freeze_account
from utils.email_warning import send_email
from page_parse.basic import is_403,is_404,is_complete
from decorators.decorator import timeout_decorator,timeout
from config.conf import get_timeout,get_crawl_interal,get_excp_interal,get_max_retries

time_out = get_timeout()
interal = get_crawl_interal()
max_retries = get_max_retries()
excp_interal = get_excp_interal()
