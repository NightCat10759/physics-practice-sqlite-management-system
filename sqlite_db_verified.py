import sqlite_handler as init


def _exercise_title_verified(exercise_title):
    
    db = init.get_db()
    correct = db.cursor().execute('select exercise_title from Exercises where exercise_title = ?;',[exercise_title]).fetchone()
    return correct

def _chapter_correct_verified(chapter_num):
    db = init.get_db()
    correct = db.cursor().execute('select chapter_num from Chapter where chapter_num = ?;',[chapter_num]).fetchone()
    return correct