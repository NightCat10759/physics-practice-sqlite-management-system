import sqlite_db_crud as crud
import sqlite_handler as init
import sqlite_db_show as show
import sqlite_db_verified as verified

import sqlite3

def insert_chapter():
    
    chapter_title = input("chapter title:")
    chapter_num = input("chapter number:")

    db = init.get_db()

    try:
        db.cursor().execute('Insert into Chapter (chapter_title,chapter_num) values (?,?);',(chapter_title,chapter_num))
        db.commit()
        print("新增完成")
    except sqlite3.IntegrityError as e:
        print(e)



def insert_exercises():
    exercise_title = input("exercises title:")
    exercise_content = input("exercises content:")

    chapter_num = search_chapter()

    print("exercise_title:",exercise_title)
    print("exercise_content:",exercise_content)
    print("chapter_num:",chapter_num)

    db = init.get_db()
    try:
        db.cursor().execute('Insert into Exercises (chapter_num,exercise_title,exercise_content) values (?,?,?);',(chapter_num,exercise_title,exercise_content))
        db.commit()
        print("新增完成")
    except sqlite3.IntegrityError as e:
        print(e)
        


def insert_tag():
    exercise_title = search_exercise_title()
    tag = input("tag :")
    chapter_num = search_chapter()


    db = init.get_db()
    try:
        db.cursor().execute('Insert into Tag (chapter_num,exercise_title,tag) values (?,?,?);',(chapter_num,exercise_title,tag))
        db.commit()
    except:
        print("chapter or exercise title is not exist.")

    print("新增完成")

def search_chapter():
    print("which one is correct chapter num:")
    db = init.get_db()
    print("chapter_num chapter_title")

    show.show_chapter()

    chapter_num = input("chpater number:")
    
    if(verified._chapter_correct_verified(chapter_num)):
        return chapter_num
    else:
        crud._exit_()
    

def search_exercise_title():
    print("which one is the correct exercise title:")
    db = init.get_db()

    show.show_exercises()

    exercise_title = input("exercise title:")

    if(verified._exercise_title_verified(exercise_title)):
        return exercise_title
    else:
        crud._exit_()


