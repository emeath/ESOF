import os
import sqlite3
import io
import datetime
import names
import csv
from gen_random_values import *

class Connect(object):
	def __init__(self, db_name):
		try:
			#conectando...
			self.conn = sqlite3.connect(db_name)
			self.cursor = self.conn.cursor()
			print('Banco:', db_name)
			self.cursor.execute('SELECT SQLITE_VERSION()')
			self.data = self.cursor.fetchone()
			print('SQLite version: %s' % self.data)
		except sqlite3.Error:
			print('Erro ao abrir banco.')
			return False

	def commit_db(self):
		if self.conn:
			self.conn.commit()

	def close_sb(self):
		if self.conn:
			self.conn.close()
			print('Conexao fechada.')

class ClientesDb(object):

	tb_name = 'clientes'

	def __init__(self):
		self.db = Connect('clientes.db')
		self.tb_name

	def fechar_conexao(self):
		self.db.close_db()

	def criar_schema(self, schema_name='clientes_schema.sql'):
		print('Criando tabela %s ...' % self.tb_name)
		try:
			with open(schema_name, 'rt') as f:
				schema = f.read()
				self.db.cursor.executescript(schema)
		except sqlite3.Error:
			print('Aviso: A tabela %s já existe.' % self.tb_name)
			return False
		print('Tabela %s criada com sucesso.' % self.tb_name)

	def inserir_um_registro(self):
		try:
			self.db.cursor.execute("""
				INSERT INTO clientes (nome, idade, cpf, email, fone, cidade, uf, criado_em)
				VALUES ('Regis da Silva', 35, '1234567890', 'regis@email.com', '(11) 9876-5342', 'Sao Paulo', 'SP', '2014-07-30 11:23:00.199000')
				""")
			# gravando no bd
			self.db.commit_db()
			print('Um registro inserido com sucesso.')
		except sqlite3.IntegrityError:
			print('Aviso: o email deve ser unico.')
			return False

	def inseir_com_lista(self):
		# criando uma lista de dados
		lista = [
					('Agenor de Sousa', 23, '12345678901', 'agenor@email.com',
					'(10) 8300-0000', 'Salvador', 'BA', '2014-07-2911:23:01.199001'),
					('Bianca Antunes', 21, '12345678902', 'bianca@email.com',
					'(10) 8350-0001', 'Fortaleza', 'CE', '2014-07-28 11:23:02.199002'),
					('Carla Ribeiro', 30, '12345678903', 'carla@email.com',
					'(10) 8377-0002', 'Campinas', 'SP', '2014-07-28 11:23:03.199003'),
					('Fabiana de Almeida', 25, '12345678904', 'fabiana@email.com',
					'(10) 8388-0003', 'São Paulo', 'SP', '2014-07-29 11:23:04.199004'),
				]

		try:
			self.sb.cursor.executemany("""

			INSERT INTO clientes (nome, idade, cpf, email, fone, cidade, uf, criado_em)
			VALUES (?,?,?,?,?,?,?,?)
			""", lista)
			# gravando no bd
			self.db.commit_db()
			print('Dados inseridos da lista com sucesso: %s registros.' % len(lista))

		except sqlite3.IntegrityError:
			print('Aviso: o email deve ser unico.')
			return False

	def inserir_com_parametros(self):
		# solicitando os dados ao usuario
		self.nome = input('Nome: ')
		self.idade = input('Idade: ')
		self.cpf = input('CPF: ')
		self.email = input('Email: ')
		self.fone = input('Fone: ')
		self.cidade = input('Cidade: ')
		self.uf = input('UF: ') or 'SP'
		date = datetime.datetime.now().isoformat(' ')
		self.criado_em = input('Criado em (%s): ' % date) or date

		try:
			self.db.cursor.execute("""
			INSERT INTO clientes (nome, idade, cpf, email, fone, cidade, uf, criado_em)
			VALUES (?, ?, ?, ?, ?, ?, ?, ?)
			""", (self.nome, self.idade, self.cpf, self.email, self.fone, self.cidade, self.uf, self.criado_em))

			#gravando no bd
			self.db.commit_db()
			print('Dados inseridos com sucesso.')
		except sqlite3.IntegrityError:
			print('Aviso: o email deve ser unico.')
			return False


	def inserir_randomico(self, repeat = 10):
		''' Inserir registros com valores randomicos names '''
		lista = []
		for _ in range(repeat):
			date = datetime.datetime.now().isoformat(' ')
			fname = names.get_first_name()
			lname = names.get_last_name()
			name = fname + ' ' + lname
			email = fname[0].lower() + '.' + lname.lower() + '@email.com'
			c = gen_city()
			city = c[0]
			uf = c[1]
			lista.append((name, gen_age(), gen_cpf(), email, gen_phone(), city, uf, date))

		try:
			self.db.cursor.executemany("""
			INSERT INTO clientes (nome, idade, cpf, email, fone, cidade, uf, criado_em)
			VALUES (?, ?, ?, ?, ?, ?, ?, ?)
				""", lista)
			self.db.commit_db()
			print('Inserindo %s registros na tabela...' % repeat)
			print('Registros criados com sucesso.')
		except sqlite3.IntegrityError:
			print('Aviso: O email deve ser unico.')
			return False

	def ler_todos_clientes(self):
		sql = 'SELECT * FROM clientes ORDER BY nome'
		r = self.db.cursor.execute(sql)
		return r.fetchall()

	def imprimir_todos_clientes(self):
		lista = self.ler_todos_clientes()
		print('{:>3s} {:20s} {:<5s} {:15s} {:21s} {:14s} {:15s} {:s} {:s}'.format('id', 'nome', 'idade', 'cpf', 'email', 'fone', 'cidade', 'uf', 'criado_em'))
		for c in lista:
			print('{:3d} {:23s} {:2d} {:s} {:>25s} {:s} {:15s} {:s} {:s}'.format( c[0], c[1], c[2],
																				  c[3], c[4], c[5],	
																				  c[6], c[7], c[8]))

	def localizar_cliente(self, id):
		r = self.db.cursor.execute(
			'SELECT * FROM clientes WHERE id = ?', (id,))
		return r.fetchone()

	def imprimir_cliente(self, id):
		if self.localizar_cliente(id) == None:
			print('Nao existe cliente com o id informado.')
		else:
			print(self.localizar_cliente(id))

	def contar_clientes(self):
		r = self.db.cursor.execute(
			'SELECT COUNT(*) FROM clientes')
		print('Total de clientes: ', r.fetchone()[0])

	# Exemplo: contar clientes com idade acime da 50 anos
	def contar_cliente_por_idade(self, t = 50):
		r = self.db.cursor.execute(
			'SELECT COUNT(*) FROM clientes WHERE idade > ?', (t,))
		print('Clientes maiores que ', t, 'anos: ', r.fetchone()[0])

	# Exemplo: localizar cliente por UF
	def localizar_cliente_por_uf(self, t = 'SP'):
		resultado = self.db.cursor.execute(
			'SELECT * FROM clientes WHERE uf = ?', (t,))
		print('Clientes do estado de ', t, ': ')
		for cliente in resultado.fetchall():
			print(cliente)

	def meu_select(self, sql="SELECT * FROM clientes WHERE uf = 'RJ';"):
		r = self.db.cursor.execute(sql)

		# gravando no bd
		self.db.commit_db()
		for cliente in r.fetchall():
			print(cliente)

	def ler_arquivo(self, file_name='clientes_sp.sql'):
		with open(file_name, 'rt') as f:
			dados = f.read()
			sqlcomandos = dados.split(';')
			print('Consulta feita a partir de arquivo externo.')
			for comando in sqlcomandos:
				r = self.db.cursor.execute(comando)
				for c in r.fetchall():
					print(c)

		# gravando no bd
		self.db.commit_db()

	def atualizar(self, id):
		try:
			c = self.localizar_cliente(id)
			if c:
				# solicitando os dados ao usuario
				self.novo_fone = input('Fone: ')
				self.db.cursor.execute("""
					UPDATE clientes
					SET fone = ?
					WHERE id = ?
					""", (self.novo_fone, id,))

				#gravando no bd
				self.db.commit_db()
				print('Dados atualizados com sucesso.')
			else:
				print('Nao existe cliente com o id informado.')
		except e:
			raise e

	def delete(self, id):
		try:
			c = self.localizar_cliente(id)
			# verificando se existe cliente com o ID passado, caso exista
			if c:
				self.db.cursor.execute("""
					DELETE FROM clientes WHERE id = ?
					""", (id,))

				# gravando no bd
				self.db.commit_db()
				print('Registro %d excluido com sucesso.' % id)
			else:
				print('Nao existe cliente com o codigo informado.')
		except e:
			raise e

	def alterar_tabela(self):
		try:
			self.db.cursor.execute("""
				ALTER TABLE clientes
				ADD COLUMN bloqueado BOOLEAN;
				""")

			# gravando no bd
			self.db.commit_db()
			print('Novo campo adicionado com sucesso.')
		except sqlite3.OperationalError:
			print("Aviso: O campo 'bloqueado' ja existe.")
			return False





if __name__ == '__main__':
	c = ClientesDb()
	c.criar_schema()
	c.inserir_um_registro()