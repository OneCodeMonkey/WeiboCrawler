# -*- coding=UTF-8 -*-
from db.basic_db import db_session
from decorators.decorator import db_commit_decorator


@db_commit_decorator
def save_relations(relations):
    db_session.add_all(relations)
    db_session.commit()
