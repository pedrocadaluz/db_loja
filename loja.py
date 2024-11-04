import sqlite3 as sql

con = sql.connect('loja.db')
cur = con.cursor()
cur.execute('DROP TABLE IF EXISTS products')
cur.execute('''CREATE TABLE products (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    NOME TEXT,
    PRECO DECIMAL(10, 2),
    QUANTIDADE INTEGER
)''')
con.commit()
con.close()
