import sqlite_db_delete_inc as delete_inc
import sqlite_db_controller as crud

def delete_chapter():
        # 選擇全刪 或是 刪其中一個資料列
        # 刪除前要先查看是否該章節有習題存在
        print("---刪除章節---")
        while(1):
                print("delete all(da) delete one(do) quit(q)")
                op = input("輸入操作:")
                switch = {
                        "da" : delete_inc.delete_all
                        ,
                        "do" : delete_inc.delete_one
                        ,
                        'q' :  crud._exit_
                }

#                try:
                out = switch.get(op)("chapter")
#                        if out == 1:
#                                break
#                except:
#                        print("沒有這個指令 insert")
#                        continue

def delete_exercises():
        # 選擇全刪 或是 刪其中一個資料列
        # 刪除前要先查看是否該章節有習題存在
        print("---刪除習題---")
        while(1):
                print("delete all(da) delete one(do) quit(q)")
                op = input("輸入操作:")
                switch = {
                        "da" : delete_inc.delete_all
                        ,
                        "do" : delete_inc.delete_one
                        ,
                        'q' :  crud._exit_
                }

#                try:
                out = switch.get(op)("exercises")
#                        if out == 1:
#                                break
#                except:
#                        print("沒有這個指令 insert")
#                        continue

def delete_tag():
        # 選擇全刪 或是 刪其中一個資料列
        # 刪除前要先查看是否該章節有習題存在
        print("---刪除標籤---")
        while(1):
                print("delete all(da) delete one(do) quit(q)")
                op = input("輸入操作:")
                switch = {
                        "da" : delete_inc.delete_all
                        ,
                        "do" : delete_inc.delete_one
                        ,
                        'q' :  crud._exit_
                }

#                try:
                out = switch.get(op)("tag")
#                        if out == 1:
#                                break
#                except:
#                        print("沒有這個指令 insert")
#                        continue
