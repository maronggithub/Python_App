"""
A program that instore the informaiton of the books which you plane to read this year
Title, Language, Type, Deadline

User can:
View all the records of the books
Search an entry
Add entry
Update entry
Delete
Close
"""
from tkinter import *

from backend import Database

database=Database("books.db")

def get_selected_row(event):
    try:

        global selected_tuple
        index=list1.curselection()[0]
        selected_tuple=list1.get(index)
        e1.delete(0,END)
        e1.insert(END,selected_tuple[1])
        e2.delete(0,END)
        e2.insert(END,selected_tuple[2])
        e3.delete(0,END)
        e3.insert(END,selected_tuple[3])
        e4.delete(0,END)
        e4.insert(END,selected_tuple[4])
    except IndexError:
        pass

def view_command():
    list1.delete(0,END)
    for row in database.view():
        list1.insert(END,row)

def search_command():
    list1.delete(0,END)
    for row in database.search(title_text.get(),language_text.get(),book_type_text.get(),deadline_text.get()):
        list1.insert(END,row)

def add_command():
    database.insert(title_text.get(),language_text.get(),book_type_text.get(),deadline_text.get())
    list1.delete(0,END)
    list1.insert(END,(title_text.get(),language_text.get(),book_type_text.get(),deadline_text.get()))

def delete_command():
    database.delete(selected_tuple[0])

def update_command():
    database.update(selected_tuple[0],title_text.get(),language_text.get(),book_type_text.get(),deadline_text.get())

window=Tk()

window.wm_title("Books Plane To Read")
#create the labels about information of the database
l1=Label(window,text="Title")
l1.grid(row=0,column=0)

l2=Label(window,text="Language")
l2.grid(row=0,column=2)

l3=Label(window,text="Type")
l3.grid(row=1,column=0)

l4=Label(window,text="Deadline")
l4.grid(row=1,column=2)
# Create the entry place where you can entry the information of the books
title_text=StringVar()
e1=Entry(window,textvariable=title_text)
e1.grid(row=0,column=1)

language_text=StringVar()
e2=Entry(window,textvariable=language_text)
e2.grid(row=0,column=3)

book_type_text=StringVar()
e3=Entry(window,textvariable=book_type_text)
e3.grid(row=1,column=1)

deadline_text=StringVar()
e4=Entry(window,textvariable=deadline_text)
e4.grid(row=1,column=3)

list1=Listbox(window, height=6,width=35)
list1.grid(row=2,column=0,rowspan=6,columnspan=2)

#Create teh scrollbar
sb1=Scrollbar(window)
sb1.grid(row=2,column=2,rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

list1.bind('<<ListboxSelect>>',get_selected_row)

#Create four function button
b1=Button(window,text="View all", width=12,command=view_command)
b1.grid(row=2,column=3)

b2=Button(window,text="Search entry", width=12,command=search_command)
b2.grid(row=3,column=3)

b3=Button(window,text="Add entry", width=12,command=add_command)
b3.grid(row=4,column=3)

b4=Button(window,text="Update selected", width=12,command=update_command)
b4.grid(row=5,column=3)

b5=Button(window,text="Delete selected", width=12,command=delete_command)
b5.grid(row=6,column=3)

b6=Button(window,text="Close", width=12,command=window.destroy)
b6.grid(row=7,column=3)
window.mainloop()
