

import sqlite3

conn = sqlite3.connect('Myfiles.db')


"""Creating a table was not
    explicitly requested in the assignment
    but I chose to create one for the sake of
    practice and organization"""

with conn:
    cur = conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS tbl_files(\
        ID INTEGER PRIMARY KEY AUTOINCREMENT,\
        file_name TEXT, \
        file_type TEXT \
        )')
    conn.commit()
conn.close()



conn = sqlite3.connect('Myfiles.db')

with conn:
    cur = conn.cursor()
    cur.execute('INSERT INTO tbl_files(file_name, file_type) VALUES (?,?)',\
                 ('information.docx', 'docx'))
    cur.execute('INSERT INTO tbl_files(file_name, file_type) VALUES (?,?)',\
                 ('hello.txt', 'txt'))
    cur.execute('INSERT INTO tbl_files(file_name, file_type) VALUES (?,?)',\
                 ('myImage.png', 'png'))
    cur.execute('INSERT INTO tbl_files(file_name, file_type) VALUES (?,?)',\
                 ('myMovie.mpg', 'mpg'))
    cur.execute('INSERT INTO tbl_files(file_name, file_type) VALUES (?,?)',\
                 ('world.txt', 'txt'))
    cur.execute('INSERT INTO tbl_files(file_name, file_type) VALUES (?,?)',\
                 ('data.pdf', 'pdf'))
    cur.execute('INSERT INTO tbl_files(file_name, file_type) VALUES (?,?)',\
                 ('myPhoto.jpg', 'jpg'))
    conn.commit()
conn.close()
    

