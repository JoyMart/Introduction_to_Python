
import sqlite3
import os

conn = sqlite3.connect('assign2.db')


with conn:
        cur = conn.cursor()
        cur.execute('CREATE TABLE IF NOT EXISTS tbl_textFiles( \
               col_id INTEGER PRIMARY KEY AUTOINCREMENT, \
               col_string TEXT \
              )' )
        conn.commit
conn.close()


dir1 = r"C:\\Users\\joybe\\Python\\python_assignments\\"
                        
file_list = []
for filename in os.listdir(dir1):
        if filename.endswith('.txt'):
                file_list.append(filename)
                print(os.path.join(dir1, filename))
        else:
                continue
print(file_list)


conn = sqlite3.connect('assign2.db')
with conn:
        cur = conn.cursor()
        cur.execute("INSERT INTO tbl_textFiles (col_string) VALUES( ?)", \
                    (file_list[0], ))
        cur.execute("INSERT INTO tbl_textFiles (col_string) VALUES( ?)", \
                    (file_list[1], ))
        cur.execute("INSERT INTO tbl_textFiles (col_string) VALUES( ?)", \
                    (file_list[2], ))
        conn.commit()
conn.close()


















