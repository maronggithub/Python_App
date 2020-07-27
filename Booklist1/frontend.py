from tkinter import *
import sqlite3

window = Tk()
#create a database table

def create_table():
  conn=sqlite3.connect("book.db")
  cur=conn.cursor()
  cur.execute("CREATE TABLE IF NOT EXISTS book (item TEXT,type TEXT,language TEXT, deadline INTEGER)")
  conn.commit()
  conn.close()

def insert(item,type,language,deadline):
  conn=sqlite3.connect("book.db")
  cur=conn.cursor()
  cur.execute("INSERT INTO book VALUES (?,?,?,?),(item,type,language,deadline)")
  conn.commit()
  conn.close()



