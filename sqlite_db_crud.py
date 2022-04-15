import sqlite_db_insert as i
import sqlite_db_delete as d
import sqlite_db_show as s

def insert():
    print("---新增---")
    print("新增章節資料(c) 新增習題資料(e) 新增標籤資料(t) 離開(q)")
    while(1):
        op = input("輸入操作:")
        switch = {
            'c' : i.insert_chapter
            ,
            'e' : i.insert_execises
            ,
            't' : i.insert_tag
            ,
            'q' :  _exit_
        }

        try:
            out = switch.get(op)()
            if out == 1:
                break
        except:
            print("沒有這個指令 insert")
            continue

        



def revise():
    print("---修改---")
    print("修改章節資料(c) 修改習題資料(e) 修改標籤資料(t) 離開(q)")
    while(1):
        op = input("輸入操作:")
        switch = {
            'c' : i.revise_chapter
            ,
            'e' : i.revise_execises
            ,
            't' : i.revise_tag
            ,
            'q' :  _exit_
        }

        try:
            out = switch.get(op)()
            if out == 1:
                break
        except:
            print("沒有這個指令")
            continue

def delete():
    print("---刪除---")
    print("刪除章節資料(c) 刪除習題資料(e) 刪除標籤資料(t) 離開(q)")
    while(1):
        op = input("輸入操作:")
        switch = {
            'c' : d.delete_chapter
            ,
            'e' : d.delete_execises
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
    print("查看章節資料(c) 查看習題資料(e) 查看標籤資料(t) 查看所有習題(a) 離開(q)")
    while(1):
        op = input("輸入操作:")
        switch = {
            'c' : s.show_chapter
            ,
            'e' : s.show_execises
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
            print("沒有這個指令")
            continue


def _exit_():
    print("離開")
    return 1
