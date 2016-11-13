# 02_create_schema.py
import sqlite3

# conectando...
conn = sqlite3.connect('clientes.db')

#definindo um cursos
cursos = conn.cursor()

#criando a tabela (schema)
cursos.execute("""
					CREATE TABLE clientes
						(
							id 			INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
							nome 		TEXT,
							idade 		INTEGER,
							cpf 		VARCHAR(11),
							email 		TEXT,
							fone 		TEXT,
							cidade 		TEXT,
							uf 			VARCHAR(2),
							criado_em 	DATE
						);
			    """)

print('Tabela criada com sucesso.')

#desconectando...
conn.close()