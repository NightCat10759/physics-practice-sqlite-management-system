import sqlite_db_crud as crud
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
            print("chapter(c) chapter_name(n) 離開(q)")
            op = input("輸入操作:")
            switch = {
                'c' : "chapter"
                ,
                'n' : "chapter_name"
                ,
                'q' : crud._exit_
            }

            try:
                out = switch.get(op)
                if out == 1:
                    break
            except:
                print("沒有這個指令 revise")
                continue
                
    if out == "chapter" :

    elif out == "chapter_name":



def revise_exercises():
    print("Input the chapter which you want to revise:")
    chapter_num = search.search_chapter()

    print("which content do you want to revise ?")
    while(1):
        print("title(t) content(c) answer(a) 離開(q)")
        op = input("輸入操作:")
        switch = {
            'c' : r.revise_chapter
            ,
            'e' : r.revise_exercises
            ,
            't' : r.revise_tag
            ,
            'q' :  _exit_
        }

        try:
            out = switch.get(op)()
            if out == 1:
                break
        except:
            print("沒有這個指令 revise")
            continue

    print("exercise_title:",exercise_title)
    print("exercise_content:",exercise_content)
    print("answer:",answer)


    db = init.get_db()
    try:
        db.cursor().execute('Insert into Exercises (chapter_num,exercise_title,answer,exercise_content) values (?,?,?,?);',(chapter_num,exercise_title,answer,exercise_content))
        db.commit()
        print("習題新增完成")
    except sqlite3.IntegrityError as e:
        print(e)
        


def revise_tag():
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



