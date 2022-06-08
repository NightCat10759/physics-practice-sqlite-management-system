# 管理sqlite資料庫
#  CRUD

import os
import sqlite3

from flask import Flask
from flask import g
from flask_script import Manager

import sqlite_db_controller as crud


app = Flask(__name__)
manager = Manager(app)

DATABASE = "test3.db"

def get_db():
#    db = getattr(g, '_database', None)
    db = None
    if db is None:
        db = sqlite3.connect(DATABASE)
        # Enable foreign key check
        db.execute("PRAGMA foreign_keys = ON")
    return db

def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()

def remove_db():
    if os.path.isfile(DATABASE):
        os.remove(DATABASE) 


def read_db():
    db = get_db()
    for chapter in db.cursor().execute('select * from Chapter'):
        print(chapter)

def _help_():
    print("新增 (i) 修改(r) 刪除(d) 查看(s) 離開(q)")


if __name__ == '__main__':
    print("這是 Physics-practice 的資料庫管理系統")
    
    while(1):
        _help_()
        print("---首頁---")
        op = input("輸入操作:")

        switch = {
            'init' : init_db
            ,
            'remove' : remove_db
            ,
            'i' : crud.insert
            ,
            'r' : crud.revise
            ,
            'd' : crud.delete
            ,
            's' : crud.show
            ,
            'q' : crud._exit_
        }

        try:
            out = switch.get(op)()
            if out == 1:
                break
        except:
            print("沒有這個指令 help(h)")
            continue

