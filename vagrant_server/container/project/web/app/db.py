# http://flask.pocoo.org/docs/1.0/tutorial/database/
import pymysql.cursors

import click
from flask import current_app, g
from flask.cli import with_appcontext

#flask g について
#https://python.ms/context/#_4-4-%E3%81%A4%E3%81%AE%E3%82%AF%E3%82%99%E3%83%AD%E3%83%BC%E3%83%8F%E3%82%99%E3%83%AB%E5%A4%89%E6%95%B0
def get_db():
    g.conn = pymysql.connect(
                host='host',
                user='user',
                password='password',
                db='db',
                cursorclass=pymysql.cursors.DictCursor
                )
    return g.conn


