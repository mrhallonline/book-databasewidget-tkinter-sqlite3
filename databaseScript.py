import sqlite3

def create_table():
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS books (title TEXT, author TEXT, published INTEGER, isbn TEXT)")
    conn.commit()
    conn.close()
    
def view_table():
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM books")
    rows=cur.fetchall()
    conn.close()
    return rows

def add_to_table(title, author, published, isbn):
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO books VALUES (?,?,?,?)",(title, author, published, isbn))
    conn.commit()
    conn.close()

create_table()
add_to_table("Concrete Blonde","Michael Connelly",2010, "0316120413")
print(view_table())