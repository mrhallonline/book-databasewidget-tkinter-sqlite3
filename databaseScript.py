import sqlite3

conn=sqlite3.connect("books.db")
cur=conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS books (title TEXT, author TEXT, published INTEGER, isbn INTEGER)")
conn.commit()
conn.close()