import sqlite3

class Database:

    def __init__(self, db):
        self.conn=sqlite3.connect(db)
        self.cur=self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS booklist (id INTEGER PRIMARY KEY, title text, language text, book_type integer, deadline integer)")
        self.conn.commit()

    def insert(self,title,language,book_type,deadline):
        self.cur.execute("INSERT INTO booklist VALUES (NULL,?,?,?,?)",(title,language,book_type,deadline))
        self.conn.commit()

    def view(self):
        self.cur.execute("SELECT * FROM booklist")
        rows=self.cur.fetchall()
        return rows

    def search(self,title="",language="",book_type="",deadline=""):
        self.cur.execute("SELECT * FROM booklist WHERE title=? OR language=? OR book_type=? OR deadline=?", (title,language,book_type,deadline))
        rows=self.cur.fetchall()
        return rows

    def delete(self,id):
        self.cur.execute("DELETE FROM booklist WHERE id=?",(id,))
        self.conn.commit()

    def update(self,id,title,language,book_type,deadline):
        self.cur.execute("UPDATE booklist SET title=?, language=?, book_type=?, deadline=? WHERE id=?",(title,language,book_type,deadline,id))
        self.conn.commit()

    def __del__(self):
        self.conn.close()

#insert("The Sun","John Smith",1918,913123132)
#delete(3)
#update(4,"The moon","John Smooth",1917,99999)
#print(view())
#print(search(language="John Smooth"))
