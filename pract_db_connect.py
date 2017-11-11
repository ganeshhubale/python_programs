import sqlite3
conn = sqlite3.connect('example.db')
c = conn.cursor()
c.execute('''CREATE TABLE stock (date text, transe text, symbol text, qty real, price real)''')

c.execute("INSERT INTO stocks VALUES('2006', 'buy', 'RHAT', 100, 22.3)")

conn.commit()

conn.close()
