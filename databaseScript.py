import sqlite3

def create_table():
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS books (title TEXT, author TEXT, published INTEGER, isbn TEXT)")
    conn.commit()
    conn.close()
    
def view_all():
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
    
def update_selected(title, author, published, isbn):
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("UPDATE books SET title=?, author=?, published=?, isbn=?"(title, author, published, isbn))
    conn.commit()
    conn.close()
    
def delete_selected(item):
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM books WHERE item = ?"(item,))
    conn.commit()
    conn.close()
    

if __name__ == "__main__":
    # add_to_table("NewTitle","NewAuth", 2020, "0316533213")
    print(view_all())