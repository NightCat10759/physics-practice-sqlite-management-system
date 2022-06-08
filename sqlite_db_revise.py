import sqlite_db_controller as crud
import sqlite_handler as init
import sqlite_db_show as show
import sqlite_db_search as search
import sqlite_db_verified as verified

import sqlite3

def revise_chapter():
    print("Input the Chapter which you want to revise?")
    chapter_num = search.search_chapter()

    print("which content do you want to revise?")
    while(1):
            print("chapter(c) chapter_title(n) 離開(q)")
            op = input("輸入操作:")
            switch = {
                'c' : "chapter"
                ,
                'n' : "chapter_title"
                ,
                'q' : crud._exit_
            }

            try:
                out = switch.get(op)
                if out == 1 or out == "chapter" or out == "chapter_title":
                    break

            except:
                print("沒有這個指令 revise")
                continue

    if out == "chapter" :
        new_chapter_num = input("Input new chapter num:")
        db = init.get_db()
        try:
            db.cursor().execute('UPDATE Chapter \
                                 SET chapter_num = ?\
                                 where chapter_num = ?',(new_chapter_num,chapter_num))
            db.commit()
            print("章節修改完成")
        except sqlite3.IntegrityError as e:
            print(e)
    elif out == "chapter_title":
        new_chapter_title = input("Input new chapter title:")
        db = init.get_db()
        try:
            db.cursor().execute('UPDATE Chapter \
                                 SET chapter_title = ?\
                                 where chapter_num = ?',(new_chapter_title,chapter_num))
            db.commit()
            print("章節名稱修改完成")
        except sqlite3.IntegrityError as e:
            print(e)
    else:
        print("ERROR")



def revise_exercises():
    print("Input the exercise title which you want to revise?")
    exercise_title = search.search_exercise_title()

    print("which content do you want to revise?")
    while(1):
            print("exercise_title(et) answer(a) exercise_content(ec) 離開(q)")
            op = input("輸入操作:")
            switch = {
                'et' : "exercise_title"
                ,
                'a' : "answer"
                ,
                'ec' : "exercise_content"
                ,
                'q' : crud._exit_
            }

            try:
                out = switch.get(op)
                if out == 1 or out == "exercise_title" or out == "answer" or out == "exercise_content":
                    break

            except:
                print("沒有這個指令 revise")
                continue

    if out == "exercise_title" :
        new_exercise_title = input("Input new exercise title:")
        db = init.get_db()
        try:
            db.cursor().execute('UPDATE Exercises \
                                 SET exercise_title = ?\
                                 where exercise_title = ?',(new_exercise_title,exercise_title))
            db.commit()
            print("習題名稱修改完成")
        except sqlite3.IntegrityError as e:
            print(e)

    elif out == "answer":
        new_answer = input("Input new answer:")
        db = init.get_db()
        try:
            db.cursor().execute('UPDATE Exercises \
                                 SET answer = ?\
                                 where exercise_title = ?',(new_answer,exercise_title))
            db.commit()
            print("習題答案修改完成")
        except sqlite3.IntegrityError as e:
            print(e)

    elif out == "exercise_content":
        new_exercise_content = input("Input new exercise content:")
        db = init.get_db()
        try:
            db.cursor().execute('UPDATE Exercises \
                                 SET exercise_content = ?\
                                 where exercise_title = ?',(new_exercise_content,exercise_title))
            db.commit()
            print("習題內容修改完成")
        except sqlite3.IntegrityError as e:
            print(e)
    else:
        print("ERROR")

def revise_tag():
    print("Input the exercise title which you want to revise?")
    exercise_title = search.search_tag()

    new_tag = input("Input new tag you want:")
    db = init.get_db()
    try:
        db.cursor().execute('UPDATE Tag \
                             SET tag = ?\
                             where exercise_title = ?',(new_tag,exercise_title))
        db.commit()
        print("習題標籤修改完成")
    except sqlite3.IntegrityError as e:
        print(e)