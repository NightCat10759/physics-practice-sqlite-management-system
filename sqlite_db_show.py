import sqlite_handler as init

def show_chapter():
    db = init.get_db()
    print("\n查看所有章節")
    print("(chapter,chapter_name)")
    for chapter in db.cursor().execute('select * from Chapter'):
        print(chapter)
    print("查看完成")

def show_exercises():
    db = init.get_db()
    print("\n查看所有習題")
    print("(id,chapter,exercise_title,answer,exercise_content)")
    for exercise_content in db.cursor().execute('select * from Exercises'):
        print(exercise_content) 
    print("查看完成")

def show_tag():
    db = init.get_db()
    print("\n查看所有標籤")
    print("(id,chapter,exercise_title,tag)")
    for tag in db.cursor().execute('select * from Tag'):
        print(tag)
    print("查看完成")

def show_all():
    db = init.get_db()

    print("\n查看所有資料")
    show_chapter()
    show_exercises()
    show_tag()