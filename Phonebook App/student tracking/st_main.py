#   Carolina Espinosa Priolo
#
#   This program is built to track student information
#   in an institution. User should be able to add and/or delete
#   student information.



from tkinter import *
import tkinter as tk
from tkinter import messagebox


#my modules
import st_gui
import st_func


#Below is the Tkinter frame class; this is the parent class
class Parent_Window(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        #master frame config
        self.master = master
        self.master.minsize(500, 500)
        self.master.maxsize(500, 500)
        self.master.title('Student Files')
        self.master.config(bg='#F0F0F0')
        self.master.protocol('WM_DELETE_WINDOW', lambda: st_func.ask_quit(self))
        arg = self.master

        st_gui.load_gui(self)

        menubar = Menu(self.master)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_separator()
        filemenu.add_command(label = 'Exit', underline=1, command=lambda: st_func.ask_quit(self))
        menubar.add_cascade(label = 'File', underline=0, menu = filemenu)


        self.master.config(menu=menubar, borderwidth='1')



        


if __name__ == '__main__':
    root = tk.Tk()
    App = Parent_Window(root)
    root.mainloop()


