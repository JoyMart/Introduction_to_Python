#
#
#
#               sqlite assignment
#
#


import sqlite3

peopleVal = (('Ron', 'Obvious', 43), ('Jane', 'Woodhouse', 37), ('Arthur', 'Belling', 28))

with sqlite3.connect('test_database.db') as conn:
        c = conn.cursor()
        c.execute("""DROP TABLE IF EXISTS People""")
        c.execute("""CREATE TABLE if not exists People(fname TEXT, lname TEXT, age INT)""")
        c.executemany("INSERT INTO People VALUES (?, ?, ?)", peopleVal)

        c.execute("SELECT fname, lname FROM People WHERE age >30")
        while True:
                row = c.fetchone()
                if row is None:
                        break
                print(row)
        































