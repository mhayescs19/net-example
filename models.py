import sqlite3 as sql
from os import path

ROOT = path.dirname(path.relpath(__file__))

def create_post(user_name, rating, location, busy, address, name, content):
    con = sql.connect(path.join(ROOT, 'database.db'))
    selector = con.cursor()

    selector.execute('insert into posts (user_name, rating, location, busy, address, name, content) values(?, ?, ?, ?, ?, ?, ?)', (user_name, rating, location, busy, address, name, content))
    con.commit()
    con.close()

def get_posts():
    con = sql.connect(path.join(ROOT, 'database.db'))
    selector = con.cursor()
    selector.execute('select * from posts')
    posts = selector.fetchall()
    return posts