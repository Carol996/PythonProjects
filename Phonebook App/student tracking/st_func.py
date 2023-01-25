#   Carolina Espinosa Priolo
#
#   This file contains all the functions
#   related to the Student Tracking program.
#   The functions in this document are called by
#   st_main.py.

import os
import tkinter import *
import tkinter as tk
import sqlite3

import st_main
import st_gui




#Displays a warning message when the user clicks X to close program
def ask_quit(self):
    if messagebox.askokcancel('Exit', 'Are you sure you want to quit the program?')
        self.master.detroy()
        os.exit(0)

#tells sql to create a db, and a table within said db
def create_db(self):
    conn = sqlite3.connect('student_records.db')
    with conn:
        cur = conn.cursor()
        cur.execute("CREATE TABLE if not exists tbl_student_records( \
            ID INTEGER PRIMARY KEY AUTOINCREMENT, \
            fname TEXT, \
            lname TEXT, \
            phone TEXT, \
            email TEXT, \
            course TEXT, \
            );")
        conn.commit()
    conn.close()
    first_run(self)


#tells sql to add values to the table within said db
def first_run(self):
    conn = sqlite3.connect('student_records.db')
    with conn:
        cur = conn.cursor()
        cur,count = count_records(cur)
        if count < 1:
            cur.execute('INSERT INTO tbl_student_records(fname, lname, phone, email, course) VALUES(?,?,?,?,?)',('Carolina','Espinosa','3214567890','espin@email.com','102'))
            conn.commit()
        conn.close()

#coutns records
def count_records(cur):
    count = ""
    cur.execute('SELECT COUNT(*) FROM tbl_student_records')
    count = cur.fetchone()[0]
    return cur,count


#selects record in box
def onSelect(self,event):
    varList = event.widget
    select = varList.curselection()[0]
    value = varList.get(select)
    conn = sqlite3.connect('student_records.db')
    with conn:
        cursor = conn.cursor()
        cursor.execute('SELECT fname, lname, phone, email, course FROM tbl_student_records WHERE ')
        




if __name__ == '__main__':
    pass
    
    
