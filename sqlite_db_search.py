import sqlite_db_controller as crud
import sqlite_handler as init
import sqlite_db_show as show
import sqlite_db_verified as verified

import sqlite3

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

def search_tag():
    print("which one is the correct tag:")
    db = init.get_db()

    show.show_tag()

    exercise_title = input("exercise title:")

    if(verified._exercise_title_verified(exercise_title)):
        return exercise_title
    else:
        crud._exit_()