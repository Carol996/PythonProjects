
#imports sqlite3 and connects
import sqlite3

conn = sqlite3.connect('myFiles2.db')




#creates table, adds columns to said table
with conn:
    cur = conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS tbl_files(\
        ID INTEGER PRIMARY KEY AUTOINCREMENT,\
        file_name TEXT)')
    conn.commit()


#creating variable for tuple
conn = sqlite3.connect('myFiles2.db')
fileList = ('information.docx','hello.txt','myImange.png',\
            'myMovie.mpg','word.txt','data.pdf','photos.jpg',)



#loop to find .txt file
for z in fileList:
    if z.endswith('.txt'): #establishes parameter .txt
        with conn:
            cur = conn.cursor()#sql command on line below
            cur.execute('INSERT INTO tbl_files (file_name) VALUES (?)',(z,))
            print(z)

conn.close()
