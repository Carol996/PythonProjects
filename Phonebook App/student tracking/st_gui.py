#   Carolina Espinosa Priolo
#
#   This is a Tkinter GUI module used in the
#   student tracking program.

from tkinter import *
import tkinter as tk

import st_main
import st_func


''' The function defined below is called by st_main.py
    on line 33
    It defines our labels and data entry boxes.
'''

def load_gui(self):
    self.lbl_fname = tk.Label(self.master, text='First Name ')
    self.lbl_fname.grid (row=0, column=0, padx=(27,0), pady=(10,0), sticky=N+W)
    self.lbl_lname = tk.Label(self.master, text='Last Name ')
    self.lbl_lname.grid (row=2, column=0, padx=(27,0), pady=(10,0), sticky=N+W)
    self.lbl_phone = tk.Label(self.master, text='Phone ')
    self.lbl_phone.grid (row=4, column=0, padx=(27,0), pady=(10,0), sticky=N+W)
    self.lbl_email = tk.Label(self.master, text='Email ')
    self.lbl_email.grid (row=6, column=0, padx=(27,0), pady=(10,0), sticky=N+W)
    self.lbl_course = tk.Label(self.master, text='Class Code ')
    self.lbl_course.grid (row=8, column=0, padx=(27,0), pady=(10,0), sticky=N+W)
    self.lbl_stList = tk.Label(self.master, text='Student List')
    self.lbl_stList.grid(row=0, column=2, padx=(0,0), pady=(10,0), sticky=N+W)

    self.txt_fname = tk.Entry(self.master,text='')
    self.txt_fname.grid(row=1,column=0,rowspan=1,columnspan=2,padx=(30,40),pady=(0,0),sticky=N+E+W)
    self.txt_lname = tk.Entry(self.master,text='')
    self.txt_lname.grid(row=3,column=0,rowspan=1,columnspan=2,padx=(30,40),pady=(0,0),sticky=N+E+W)
    self.txt_phone = tk.Entry(self.master,text='')
    self.txt_phone.grid(row=5,column=0,rowspan=1,columnspan=2,padx=(30,40),pady=(0,0),sticky=N+E+W)
    self.txt_email = tk.Entry(self.master,text='')
    self.txt_email.grid(row=7,column=0,rowspan=1,columnspan=2,padx=(30,40),pady=(0,0),sticky=N+E+W)
    self.txt_course = tk.Entry(self.master,text='')
    self.txt_course.grid(row=9,column=0,rowspan=1,columnspan=2,padx=(30,40),pady=(0,0),sticky=N+E+W)


    #Defines Student List box
    self.scrollbar1 = Scrollbar(self.master, orient=VERTICAL)
    self.lstList1 = Listbox(self.master, exportselection=0, yscrollcommand=self.scrollbar1.set)
    self.lstList1.bind('<<ListboxSelect>>',lambda event: st_func.onSelect(self,event))
    self.scrollbar1.config(command=self.lstList1.yview)
    #Defines the size and location of Student List box and its scrolling bar
    self.scrollbar1.grid(row=1, column=5, rowspan=9, columnspan=1, padx=(0,0), pady=(0,0), sticky=N+E+S)
    self.lstList1.grid(row=1, column=2, rowspan=9, columnspan=3, padx=(0,0), pady=(0,0), sticky=N+E+S+W)

    #Defines size, placement, and commands of the buttons
    self.btn_add = tk.Button(self.master,width=13,height=2,text='Add',command=lambda: st_func.addToList(self))
    self.btn_add.grid(row=10,column=0,padx=(25,0),pady=(45,10),sticky=W)
    self.btn_update = tk.Button(self.master,width=13,height=2,text='Update',command=lambda: st_func.onUpdate(self))
    self.btn_update.grid(row=10,column=1,padx=(15,0),pady=(45,10),sticky=W)
    self.btn_delete = tk.Button(self.master,width=13,height=2,text='Delete',command=lambda: st_func.onDelete(self))
    self.btn_delete.grid(row=10,column=2,padx=(15,0),pady=(45,10),sticky=W)
    self.btn_close = tk.Button(self.master,width=13,height=2,text='Close',bg='red',command=lambda: st_func.ask_quit(self))
    self.btn_close.grid(row=10,column=4,columnspan=1,padx=(15,0),pady=(45,10),sticky=E)


    st_func.create_db(self)
    st_func.onRefresh(self)
        
    
    



if __name__ == '__main__':
    pass
