import sqlite_db_controller as crud
import sqlite_handler as init
import sqlite_db_show as show
import sqlite_db_search as search
import sqlite_db_verified as verified

import sqlite3

def insert_chapter():
    
    chapter_title = input("chapter title:")
    chapter_num = input("chapter number:")

    db = init.get_db()

    try:
        db.cursor().execute('Insert into Chapter (chapter_title,chapter_num) values (?,?);',(chapter_title,chapter_num))
        db.commit()
        print("章節新增完成")
    except sqlite3.IntegrityError as e:
        print(e)



def insert_exercises():
    exercise_title = input("exercises title:")
    exercise_content = input("exercises content:")
    answer = input("exercises answer:")

    chapter_num = search.search_chapter()

    print("exercise_title:",exercise_title)
    print("exercise_content:",exercise_content)
    print("answer:",answer)
    print("chapter_num:",chapter_num)

    db = init.get_db()
#    try:
    db.cursor().execute('Insert into Exercises (chapter_num,exercise_title,answer,exercise_content) values (?,?,?,?);',(chapter_num,exercise_title,answer,exercise_content))
    db.commit()
    print("習題新增完成")
#    except sqlite3.IntegrityError as e:
#    print(e)
        


def insert_tag():
    exercise_title = search.search_exercise_title()
    tag = input("tag :")
    chapter_num = search.search_chapter()


    db = init.get_db()
    try:
        db.cursor().execute('Insert into Tag (chapter_num,exercise_title,tag) values (?,?,?);',(chapter_num,exercise_title,tag))
        db.commit()
        print("標籤新增完成")
    except:
        print("chapter or exercise title is not exist.")



