#   Carolina Espinosa Priolo
#
#   This program is designed to transfer files from
#   one directory to another.
#

import tkinter as tk
from tkinter import *

import tkinter.filedialog

import os
import shutil
import time
import datetime
from datetime import datetime, timedelta



#creates the window, give it a name
class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self)
        self.master.title("File Transfer")

        
        #creates a button to select files
        self.sourceDir_btn = Button(text = "Select Source", width=20, command=self.sourceDir)
        self.sourceDir_btn.grid(row=0, column=0, padx=(20,10), pady=(30,0))

        #creates entry for source dir selection and positions it
        self.source_dir = Entry(width=75)
        self.source_dir.grid(row=0, column=1, columnspan=2, padx=(20,10), pady=(30,0))


        #creates button to select destination for files selected
        self.destDir_btn = Button(text="Select Destination", width=20, command=self.destDir)
        self.destDir_btn.grid(row=1, column=0, padx=(20,10), pady=(15,10))

        #creates entry for directory selection
        self.destination_dir = Entry(width=75)
        self.destination_dir.grid(row=1, column=1, columnspan=2, padx=(20,10), pady=(15, 10))


        self.transfer_btn = Button(text="Transfer Files", width=20, command=self.transferFiles)
        self.transfer_btn.grid(row=2, column=1, padx=(200, 0), pady=(0,15))

        #exit btn
        self.exit_btn = Button(text="Exit", width=20, command=self.exit_program)
        self.exit_btn.grid(row=2, column=2, padx=(10, 40), pady=(0, 15))


    #creates function to select src dir
    def sourceDir(self):
        selectSourceDir = tkinter.filedialog.askdirectory()
        #the .delete(0, END) will clear the content inserted in the entry widget
        #this allows the path to be inserted into the entry widget properly
        self.source_dir.delete(0, END)
        #the .insert method will insert the user selection to the source_dir Entry
        self.source_dir.insert(0, selectSourceDir)


    #creates function to select dest dir
    def destDir(self):
        selectDestDir = tkinter.filedialog.askdirectory()
        self.destination_dir.delete(0, END)
        self.destination_dir.insert(0, selectDestDir)


    def transferFiles(self):
        #gets source dir, lists source files
        source = self.source_dir.get()
        source_files = os.listdir(source)

        #gets dest dir
        destination = self.destination_dir.get()


        #runs thru each file in source dir
        for i in source_files:

            #defines vars for current time minus 24 hrs
            t = datetime.datetime.now()
            cutoff = t - timedelta(hours=24)

            #defines var for file's timestamp
            mtime = os.path.getmtime(i)

            #transfers files if their timestamp is less than or equal to 24 hrs
            if mtime <= cutoff:
                shutil.move(source + '/' + i, destination)
                print(i + ' was successfully transferred')      

    


    '''  ORIGINAL CODE BELOW

    #creates function to transfer files from one directory to another
    def transferFiles(self):
        #gets source and dest dir
        source = self.source_dir.get()
        destination = self.destination_dir.get()

        #gets list of files in the src dir
        source_files = os.listdir(source)

        #runs through each file in the source dir
        for i in source_files:
            #moves each file from src to dest
            shutil.move(source + '/' + i, destination)
            print(i + ' was successfully transferred.')'''            
    

      
    #creates function to exit program
    def exit_program(self):
        root.destroy()

           



if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
