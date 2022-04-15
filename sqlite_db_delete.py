import sqlite_handler as init
import sqlite_db_crud as crud
import sqlite_db_show as show
import sqlite_db_verified as verified

def delete_all(topic):
        # 全部刪除
        if(topic == "chapter"):

                show.show_chapter()
                print("確認要將\"章節\"全部刪除嗎?")
                op = input("輸入(y)(n):")

                if (op == 'y'):

                        db = init.get_db()
                        db.cursor().execute('delete * from Chapter;')
                        db.commit()

                        print("章節全部刪除")
                else:
                        print("操作失敗")
                        crud._exit_()
        
                        

def delete_one(topic):
        # 刪除一行資料列
        print("---刪除章節選擇---")
        if(topic == "chapter"):

                show.show_chapter()
                print("確認要刪除的章節資料")
                chapter_num = input("(輸入 chapter_num):")

                if (verified._chapter_correct_verified(chapter_num)):
                        db = init.get_db()
                        db.cursor().execute('delete * from Chapter where chapter_num = ?;',[chapter_num])
                        db.commit()

                        print(chapter_num + " 章節刪除")
                else:
                        print("操作失敗")
                        crud._exit_()


def delete_chapter():
        # 選擇全刪 或是 刪其中一個資料列
        print("---刪除章節---")
        print("delete all(da) delete one(do) quit(q)")
        while(1):
                op = input("輸入操作:")
                switch = {
                        "da" : delete_all("chapter")
                        ,
                        "do" : delete_one("chapter")
                        ,
                        'q' :  crud._exit_()
                }

#                try:
                out = switch.get(op)()
#                        if out == 1:
#                                break
#                except:
#                        print("沒有這個指令 insert")
#                        continue

def delete_execises():
        print("delete ex")     

def delete_tag():
        print("delete tag")

def delete_all():
        db = init.get_db()
        db.cursor().execute('Insert into Tag (chapter_num,exercise_title,tag) values (?,?,?);',(chapter_num,exercise_title,tag))
        db.commit()
        print("delete tag")