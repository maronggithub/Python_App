import sqlite3

def connect():
  conn = sqlite3.connect("books.db")
  cur = conn.cursor()
  cur.execute("CREATE TABLE IF NOT EXISTS booklist (id INTEGER PRIMARY KEY, title text, language text, book_type integer, deadline integer)")
  conn.commit()
  conn.close()

def insert(title,language,book_type,deadline):
  conn = sqlite3.connect("books.db")
  cur = conn.cursor()
  cur.execute("INSERT INTO booklist VALUES (NULL,?,?,?,?)",(title,language,book_type,deadline))
  conn.commit()
  conn.close()

def view():
  conn = sqlite3.connect("books.db")
  cur = conn.cursor()
  cur.execute("SELECT * FROM booklist")
  rows= cur.fetchall()
  conn.close()
  return rows

def search(title="",language="",book_type="",deadline=""):
  conn = sqlite3.connect("books.db")
  cur = conn.cursor()
  cur.execute("SELECT * FROM booklist WHERE title=? OR language=? OR book_type=? OR deadline=?", (title,language,book_type,deadline))
  rows= cur.fetchall()
  conn.close()
  return rows

def delete(id):
  conn = sqlite3.connect("books.db")
  cur = conn.cursor()
  cur.execute("DELETE FROM booklist WHERE id=?",(id,))
  conn.commit()
  conn.close()

def update(id,title,language,book_type,deadline):
  conn = sqlite3.connect("books.db")
  cur = conn.cursor()
  cur.execute("UPDATE booklist SET title=?, language=?, book_type=?, deadline=? WHERE id=?",(title,language,book_type,deadline,id))
  conn.commit()
  conn.close()




# connect()
# insert("Telling Lies","English","Psychology",11)
# print(view())
# print(search(title="現実を見よう"))
# delete(2)
update(5,"流动的盛宴","Chinese","Novel",10)
print(search(title="流动的盛宴"))