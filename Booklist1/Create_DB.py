from tkinter import *
import sqlite3


#create a database table

def create_table():
  conn=sqlite3.connect("book.db")
  cur=conn.cursor()
  cur.execute("CREATE TABLE IF NOT EXISTS book (item Text,language TEXT,deadline INTEGER)")
  conn.commit()
  conn.close()

def insert(item,language,deadline):
  conn=sqlite3.connect("book.db")
  cur=conn.cursor()
  cur.execute("INSERT INTO book VALUES(?,?,?)",(item,language,deadline))
  conn.commit()
  conn.close()


def view():
  conn=sqlite3.connect("book.db")
  cur=conn.cursor()
  cur.execute("SELECT * FROM book")
  rows=conn.fetchall()
  conn.close()
  return rows

def delete(item):
  conn=sqlite3.connect("book.db")
  cur=conn.cursor()
  cur.execute("DELETE FROM book WHERE item=?",(item,))
  conn.commit()
  conn.close()

def update(language,deadline,item):
  conn=sqlite3.connect("book.db")
  cur=conn.cursor()
  cur.execute("UPDATE book SET language=?,deadline=? WHERE item=?,(language,deadline,item))
  conn.commit()
  conn.close()
  
# insert("In Search For Lost Time","English",12)
# print(view()) 