import tkinter
from tkinter import *


class ParentWindow(Frame):
    def __init__ (self, master):# self passes in elements of a class into functions
        Frame.__init__ (self)

        self.master = master
        self.master.resizable(width=True, height=True)#true or false values gives me the ability to resize
        self.master.geometry('{}x{}'.format(500, 400))
        self.master.title('Learning Tkinter')
        self.master.config(bg="black")

        self.varfName = StringVar()
        self.varlName = StringVar()

        self.lblfName = Label(self.master, text = 'First Name: ', font = ('Arial', 16), fg = 'green', bg='black')
        self.lblfName.grid(row = 0, column = 0, padx=(30, 0), pady=(30,0))

        self.lbllName = Label(self.master, text = 'Last Name: ', font = ('Arial', 16), fg = 'green', bg='black')
        self.lbllName.grid(row = 1, column = 0, padx=(30, 0), pady=(30,0))

        self.lblDisplay = Label(self.master, text='', font=('Helvetica', 14), fg='green', bg='black')
        self.lblDisplay.grid(row =3, column =1, padx=(30, 0), pady=(30,0))

        self.txtfName = Entry(self.master, text = self.varfName, font = ('Courier', 16), fg = 'green', bg = 'black')
        self.txtfName.grid(row =0, column =1, padx=(30, 0), pady=(30,0))

        self.txtlName = Entry(self.master, text = self.varlName, font = ('Courier', 16), fg = 'green', bg = 'black')
        self.txtlName.grid(row =1, column =1, padx=(30, 0), pady=(30,0))

        self.btnSubmit = Button(self.master, text = 'Submit', width = 10, height=2, command=self.submit)
        self.btnSubmit.grid(row=2, column=1, padx=(30,0), pady=(30,0), sticky=NE)

        self.btnCancel = Button(self.master, text = 'Cancel', width = 10, height=2, command=self.cancel)
        self.btnCancel.grid(row=2, column=1, padx=(0,90), pady=(30,0), sticky=NE)

    def submit(self):
        fn = self.varfName.get()
        ln = self.varlName.get()
        self.lblDisplay.config(text='Hi {} {}'.format(fn, ln))

    def cancel(self):
        self.master.destroy()


        


if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop() #this will make sure window stays open
