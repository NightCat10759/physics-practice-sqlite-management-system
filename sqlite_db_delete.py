import sqlite_handler as init

def show_chapter():
        print("show ch")

def show_execises():
        print("show ex")     

def show_tag():
        print("show tag")

def show_all():
    db = init.get_db()
    for chapter in db.cursor().execute('select * from Chapter'):
        print(chapter)