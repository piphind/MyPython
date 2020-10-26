import sqlite3


def connect():
    conn = sqlite3.connect("Books.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS book "
                "(id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, isbn INTEGER)")
    conn.commit()
    conn.close()


def insert(f_title, f_author, f_year, f_isbn):
    conn = sqlite3.connect("Books.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO book VALUES(NULL,?,?,?,?)", (f_title, f_author, f_year, f_isbn))
    conn.commit()
    conn.close()


def view():
    conn = sqlite3.connect("Books.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM book")
    f_rows = cur.fetchall()
    conn.close()
    return f_rows


connect()
insert("The bible", "God", 0000, 1111111111111)
print(view())
