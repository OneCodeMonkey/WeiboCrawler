import time
import datetime

from sqlalchemy import text
from sqlalchemy.exc import IntegrityError as SqlalchemyIntegrityError
from pymysql.err import IntegrityError as PymysqlIntegrityError
from sqlalchemy.exc import InvalidRequestError

from db.basic import db_session
from db.models import (
    LoginInfo, KeywordsWbdata, KeyWords, SeedIds, UserRelation,
    WeiboComment, WeiboRepost, User, WeiboData, WeiboPraise
)

db_session.query(WeiboData.uid). \
            filter(text('id>17319011')).all()