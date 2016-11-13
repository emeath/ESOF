# 08_delete_data
import sqlite3

conn = sqlite3.connect('clientes.db')
cursor = conn.cursor()

id_cliente = 8

#excluido um registro da tabela
cursor.execute("""
					DELETE FROM clientes WHERE id = ?
               """, (id_cliente,)
               )

conn.commit()

print('Registro (id = %d) excluido com sucesso.' % id_cliente)

conn.close()