import sqlite_db_insert as i
import sqlite_db_delete as d
import sqlite_db_revise as r
import sqlite_db_show as s

def insert():
    print("---新增---")
    while(1):
        print("新增章節資料(c) 新增習題資料(e) 新增標籤資料(t) 離開(q)")
        op = input("輸入操作:")
        switch = {
            'c' : i.insert_chapter
            ,
            'e' : i.insert_exercises
            ,
            't' : i.insert_tag
            ,
            'q' :  _exit_
        }

#        try:
        out = switch.get(op)()
#            if out == 1:
#                break
#        except:
#            print("沒有這個指令 insert")
#            continue

        



def revise():
    print("---修改---")
    while(1):
        print("修改章節資料(c) 修改習題資料(e) 修改標籤資料(t) 離開(q)")
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

def delete():
    print("---刪除---")
    while(1):
        print("刪除章節資料(c) 刪除習題資料(e) 刪除標籤資料(t) 離開(q)")
        op = input("輸入操作:")
        switch = {
            'c' : d.delete_chapter
            ,
            'e' : d.delete_exercises
            ,
            't' : d.delete_tag
            ,
            'q' :  _exit_
        }

#        try:
        out = switch.get(op)()
#            if out == 1:
#                break
#        except:
#            print("沒有這個指令")
#            continue
#
#        if out == 1:
#            break

def show():
    print("---查看---")
    while(1):
        print("查看章節資料(c) 查看習題資料(e) 查看標籤資料(t) 查看所有習題(a) 離開(q)")
        op = input("輸入操作:")
        switch = {
            'c' : s.show_chapter
            ,
            'e' : s.show_exercises
            ,
            't' : s.show_tag
            ,
            'a' : s.show_all
            ,
            'q' :  _exit_
        }



        try:
            out = switch.get(op)()
            if out == 1:
                break
        except:
            print("沒有這個指令 show")
            continue


def _exit_():
    print("離開")
    return 1
