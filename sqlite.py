import sqlite3

db_conector = sqlite3.connect('log-temperatura.db')

db_cursor = db_conector.cursor()

grados = 21.7
db_cursor.execute("INSERT INTO temperaturas values(datetime('now'), (?))", (grados,))
db_conector.commit()

db_conector.close()