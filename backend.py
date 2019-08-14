import sqlite3

def connect():
    conn=sqlite3.connect("items.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS ITEMLIST (id INTEGER PRIMARY KEY,name text,price integer,quantity integer)")
    conn.commit()
    conn.close()

def insert(id,name,price,quantity):
    conn=sqlite3.connect("items.db")
    cur=conn.cursor()
    cur.execute("INSERT OR IGNORE INTO ITEMLIST VALUES (?,?,?,?)",(id,name,price,quantity))
    conn.commit()
    conn.close()

def view():
    conn=sqlite3.connect("items.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM ITEMLIST")
    rows=cur.fetchall()
    conn.close()
    return rows

def search(id="",name="",price="",quantity=""):
    conn=sqlite3.connect("items.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM ITEMLIST WHERE id=? OR name=? OR price=? OR quantity=?",(id,name,price,quantity))
    rows=cur.fetchall()
    conn.close()
    return rows

def delete(id):
    conn=sqlite3.connect("items.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM ITEMLIST WHERE id=?",(id,))
    conn.commit()
    conn.close()

def update(id,name,price,quantity):
    conn=sqlite3.connect("items.db")
    cur=conn.cursor()
    cur.execute("UPDATE ITEMLIST SET name=?,price=?,quantity=? WHERE id=?",(name,price,quantity,id))
    conn.commit()
    conn.close()

connect()
#update(21,"stellseries",25000,65)
#insert(2,"genegr",21,992)
print(view())
#print(search(quantity=1))
#delete(2121)
