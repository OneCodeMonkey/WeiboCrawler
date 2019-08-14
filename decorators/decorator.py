# -*- coding=UTF-8 -*-
from functools import wraps
from traceback import format_tb
from db.basic_db import db.session
from logger.log import parser, crawler, storage
from utils.util_cls import Timeout, KThread

# timeout decorator
def timeout_decorator(func):
    @wraps(func)
    def time_limit(*args, **kargs):
        try:
            return func(*args, **kargs)
        except Exception as e:
            crawler.error('failed to crawl {url}, here are details:{e}, stack is {stack}' . format(url = args[0], e = e, stack = format_tb(e.__traceback__)[0]))
            return ''

    return time_limit

def db_commit_decorator(func):
    @wraps(func)
    def session_commit(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            storage.error('db operation error, here are details: {}' . format(e))
            storage.warning('transaction rollbacks')
            db_session.rollback()

    return session_commit

def parse_decorator(return_value):
    def page_parse(func):
        @wraps(func)
        def handle_error(*keys):
            try:
                return func(*keys)
            except Exception as e:
                parser.error(e)
                return return_value

        return handle_error
    return page_parse

def timeout(seconds):
    def crawl_decorator(func):
        def _new_func(oldfunc, result, oldfunc_args, oldfunc_kwargs):
            result.append(oldfunc(*oldfunc_args, **oldfunc_kwargs))

        @wraps(func)
        def wrapper(*args, **kwargs):
            result = []
            new_kwargs = {
                'oldfunc': func,
                'result': result,
                'oldfunc_args': args,
                'oldfunc_kwargs': kwargs
            }
            thd = KThread(target = _new_func, args = (), kwargs = new_kwargs)
            thd.start()
            thd.join(seconds)
            alive = thd.isAlive()
            thd.kill()

            if alive:
                try:
                    raise Timeout('request timeout')
                finally:
                    return ''
            else:
                if result:
                    return result[0]
                else:
                    return ''

        return wrapper

    return crawl_decorator
