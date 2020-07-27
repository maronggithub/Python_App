from tkinter import *
import sqlite3


#create a database table

def create_table():
  conn=sqlite3.connect("book.db")
  cur=conn.cursor()
  sql = '''CREATE TABLE IF NOT EXISTS apps
             (item TEXT,
              language TEXT,
              book_type TEXT,
              deadline INTEGER)'''
  cur.execute(sql)
  conn.commit()
  conn.close()

def insert(item,language,book_type,deadline):
  conn=sqlite3.connect("book.db")
  cur=conn.cursor()
  cur.execute('INSERT INTO apps VALUES (?,?,?,?)',(item,language,book_type,deadline))
  conn.commit()
  conn.close()


def view():
  conn=sqlite3.connect("book.db")
  cur=conn.cursor()
  cur.execute("SELECT * FROM apps")
  rows=cur.fetchall()
  conn.close()
  return rows

def delete(item):
  conn=sqlite3.connect("book.db")
  cur=conn.cursor()
  cur.execute("DELETE FROM apps WHERE item=?",(item,))
  conn.commit()
  conn.close()

def update(language,deadline,book_type,item):
  conn=sqlite3.connect("book.db")
  cur=conn.cursor()
  cur.execute("UPDATE apps SET language=?,deadline=?,book_type=? WHERE item=?,(language,deadline,book_type,item))
  conn.commit()
  conn.close()

# insert("流动的盛宴","Chinese","novel",9)

# print(view())