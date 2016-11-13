CREATE TABLE clientes (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	nome TEXT,
	idade INTEGER,
	cpf	VARCHAR(11),
	email TEXT,
	fone TEXT,
	cidade TEXT,
	uf VARCHAR(2),
	criado_em DATETIME
);
