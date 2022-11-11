import sqlite3


def add_to_db(question1, url1, data1):
    with sqlite3.connect('result.db') as con:
        taglist = [(question1, url1, data1)]
        cur = con.cursor()
        cur.execute(f'INSERT INTO res (question, url, data) VALUES (\"{question1}\", \"{url1}\", \"{data1}\")')



