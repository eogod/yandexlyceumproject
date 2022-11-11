import sqlite3


def add_to_db(question1, url1, data1):
    with sqlite3.connect('result.db') as con:
        cur = con.cursor()
        cur.execute(f'INSERT INTO res (question, url, data) VALUES (\"{question1}\", \"{url1}\", \"{data1}\")')



def loadbd():
    with sqlite3.connect('result.db') as con:
        cur = con.cursor()
        sqlite_select_query = "SELECT question FROM res"
        que = '\n'.join([elem for i in list(cur.execute(sqlite_select_query)) for elem in i])
        return que

