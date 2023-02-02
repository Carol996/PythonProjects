import tkinter as tk
from tkinter import *
import webbrowser


class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master.title('Web Page Generator')

        #default text button
        self.btn = Button(self.master, text="Default HTML Page", width=30, height=2, command=self.defaultHTML)
        self.btn.grid(row=2, column=0, padx=(10,10), pady=(10,10))

        #custom text button
        self.btn = Button(self.master, text="Custom HTML Page", width=30, height=2, command=self.customHTML)
        self.btn.grid(row=2, column=1, padx=(10,10), pady=(10,10))

        #information
        self.info = tk.Label(self.master, text="Please type the desired content for your site below: ")
        self.info.grid(row=0, column=0, padx=(10,0), pady=(5,0))
        
        #entry
        self.textInput = Entry(self.master, text='', width=75)
        self.textInput.grid(row=1, column=0, columnspan=3, padx=(10,10), pady=(10,10))
        

    #this function defines the default website
    def defaultHTML(self):
        htmlText = "Stay tuned for our sale"
        htmlFile = open("index.html", "w")
        htmlContent = "<html>\n<body>\n<h1>" + htmlText + "</h1>\n</body>\n</html>"
        htmlFile.write(htmlContent)
        htmlFile.close()
        webbrowser.open_new_tab("index.html")



    #this function defines the custom website
    def customHTML(self):
        htmlText = self.textInput.get()
        htmlFile = open("index.html", "w")
        htmlContent = "<html>\n<body>\n<h1>" + htmlText + "</h1>\n</body>\n</html>"
        htmlFile.write(htmlContent)
        htmlFile.close()
        webbrowser.open_new_tab("index.html")

    


        


        

            








if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
