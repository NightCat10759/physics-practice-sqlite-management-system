import sqlite_handler as init
import sqlite_db_crud as crud
import sqlite_db_show as show
import sqlite_db_verified as verified
import sqlite3

def choose_chapter_all():
        show.show_chapter()
        print("確認要將\"章節\"全部刪除嗎?")
        op = input("輸入(y)(n):")
        if (op == 'y'):
                db = init.get_db()
                try:
                        db.cursor().execute('delete from Chapter;')
                        db.commit()
                        print("章節全部刪除")
                except sqlite3.IntegrityError as e:
                        print("操作失敗: ",e)
        else:
                print("操作失敗")
                crud._exit_()

def choose_chapter_one():
        show.show_chapter()
        print("確認要刪除的章節資料")
        chapter_num = input("(輸入 chapter_num):")
        if (verified._chapter_correct_verified(chapter_num)):
                db = init.get_db()
                
                try:
                        db.cursor().execute('delete from Chapter where chapter_num = ?;',[chapter_num])
                        db.commit()
                        print(chapter_num + " 章節刪除")
                except sqlite3.IntegrityError as e:
                        print("操作失敗: ",e)
        else:
                print("操作失敗")
                crud._exit_()

def choose_exercises_all():
        show.show_exercises()
        print("確認要將\"章節\"全部刪除嗎?")
        op = input("輸入(y)(n):")
        if (op == 'y'):
                db = init.get_db()
                try:
                        db.cursor().execute('delete from Exercises;')
                        db.commit()
                        print("章節全部刪除")
                except sqlite3.IntegrityError as e:
                        print("操作失敗: ",e)
        else:
                print("操作失敗")
                crud._exit_()

def choose_exercises_one():
        show.show_chapter()
        print("確認要刪除的章節資料")
        chapter_num = input("(輸入 chapter_num):")
        if (verified._chapter_correct_verified(chapter_num)):
                db = init.get_db()
                
                try:
                        db.cursor().execute('delete from Chapter where chapter_num = ?;',[chapter_num])
                        db.commit()
                        print(chapter_num + " 章節刪除")
                except sqlite3.IntegrityError as e:
                        print("操作失敗: ",e)
        else:
                print("操作失敗")
                crud._exit_()

def choose_tag_all():
        show.show_exercises()
        print("確認要將\"章節\"全部刪除嗎?")
        op = input("輸入(y)(n):")
        if (op == 'y'):
                db = init.get_db()
                try:
                        db.cursor().execute('delete from Exercises;')
                        db.commit()
                        print("章節全部刪除")
                except sqlite3.IntegrityError as e:
                        print("操作失敗: ",e)
        else:
                print("操作失敗")
                crud._exit_()

def choose_tag_one():
        show.show_chapter()
        print("確認要刪除的章節資料")
        chapter_num = input("(輸入 chapter_num):")
        if (verified._chapter_correct_verified(chapter_num)):
                db = init.get_db()
                
                try:
                        db.cursor().execute('delete from Chapter where chapter_num = ?;',[chapter_num])
                        db.commit()
                        print(chapter_num + " 章節刪除")
                except sqlite3.IntegrityError as e:
                        print("操作失敗: ",e)
        else:
                print("操作失敗")
                crud._exit_()

def delete_all(topic):
        # 全部刪除
        print("---刪除全部章節選擇---")
        if(topic == "chapter"):
                choose_chapter_all()
        elif(topic == "exercises"):
                choose_exercises_all()
        
        elif(topic == "tag"):
                choose_tag_all()
        
        else:
                crud._exit_()
        
                        

def delete_one(topic):
        # 刪除一行資料列
        print("---刪除章節選擇---")
        if(topic == "chapter"):
                choose_chapter_one()   
        elif(topic == "exercises"):
                choose_exercises_one()   
        
        elif(topic == "tag"):
                choose_tag_one()   
        
        else:
                crud._exit_()
