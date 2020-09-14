
import sqlite3
import os

conn = sqlite3.connect('assign2.db')


with conn:
        cur = conn.cursor()
        cur.execute('CREATE TABLE IF NOT EXISTS tbl_txtFiles( \
               col_id INTEGER PRIMARY KEY AUTOINCREMENT, \
               col_files TEXT \
              )' )
        conn.commit
conn.close()

fileList = ('information.docx', 'Hello.txt', 'myImage.png', \
            'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg')
                        


conn = sqlite3.connect('assign2.db')
with conn:
        cur = conn.cursor()
        for filename in fileList:
                if filename.endswith('.txt'):
                        print(filename)
                        cur.execute("INSERT INTO tbl_txtFiles (col_files) VALUES( ?)", (filename,))
                else:
                        continue
        conn.commit()
conn.close()













