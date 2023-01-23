import tkinter
from tkinter import *


class ParentWindow(Frame):
    def __init__ (self, master):# self passes in elements of a class into functions
        Frame.__init__ (self)

        self.master = master
        self.master.resizable(width=True, height=True)#true or false values gives me the ability to resize
        self.master.geometry('{}x{}'.format(400, 400))
        self.master.title('Learning Tkinter')
        self.master.config(bg="black")

        self.varfName = StringVar()
        self.varlName = StringVar()

        self.lblfName = Label(self.master, text = 'First Name ', font = ('Arial', 16), fg = 'green', bg='black')
        self.lblfName.grid(row = 0, column = 0)

        self.lbllName = Label(self.master, text = 'Last Name ', font = ('Arial', 16), fg = 'green', bg='black')
        self.lbllName.grid(row = 0, column = 0)


        self.txtfName = Entry(self.master, text = self.varfName, font = ('Courier', 16), fg = 'green', bg = 'black')
        self.txtfName.grid(row =, column =)

        self.txtlName = Entry(self.master, text = self.varlName, font = ('Courier', 16), fg = 'green', bg = 'black')
        self.txtlName.grid(row =, column =)


if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop() #this will make sure window stays open
