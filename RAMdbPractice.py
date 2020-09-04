


import sqlite3

with sqlite3.connect(":memory:") as conn:
        c = conn.cursor()
        creatures = (('Jean-Baptiste Zorg', 'Human', 122), ('Korben Dallas', 'Meat Popsicle', 100), ("Ak\'not", 'Mangalore', -5))
        Roster = c.execute("CREATE TABLE if not exists Roster('Name' TEXT, 'Species' TEXT, 'IQ' INT)")
        c.executemany("INSERT INTO Roster VALUES (?, ?, ?)", creatures)
        print(Roster)

        c.execute("UPDATE Roster SET Species = 'Human' WHERE Name = 'Korben Dallas';")
        print(Roster)

        c.execute("SELECT Name, IQ FROM Roster WHERE Species = 'Human';")
        while True:
                row = c.fetchone()
                if row is None:
                        break
                print(row)
