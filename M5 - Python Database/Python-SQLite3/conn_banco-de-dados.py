#conn_banco-de-dados.py
#01_create_db.py
import sqlite3

conn=sqlite3.connect('clientes.db')
conn.close()
