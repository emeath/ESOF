BEGIN TRANSACTION;
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
			, bloqueado BOOLEAN);
INSERT INTO "clientes" VALUES(1,'Regis',35,'0000','regis@email.com','11-1000-2014','Sao Paulo','SP','2014-06-11',NULL);
INSERT INTO "clientes" VALUES(2,'Aloisio',87,'1111','aloisio@email.com','98765-4322','Porto Alegre','RS','2014-06-09',NULL);
INSERT INTO "clientes" VALUES(3,'Bruna',21,'2222','bruna@email.com','21-98765-4323','Rio de Janeiro','RJ','2014-06-09',NULL);
INSERT INTO "clientes" VALUES(4,'Matheus',19,'3333','matheus@email.com','11-98765-4324','Campinas','SP','2014-06-09',NULL);
INSERT INTO "clientes" VALUES(5,'Regis',35,'0000','regis@email.com','11-98765-4321','Sao Paulo','SP','2014-06-08',NULL);
INSERT INTO "clientes" VALUES(6,'Aloisio',87,'1111','aloisio@email.com','98765-4322','Porto Alegre','RS','2014-06-09',NULL);
INSERT INTO "clientes" VALUES(7,'Bruna',21,'2222','bruna@email.com','21-98765-4323','Rio de Janeiro','RJ','2014-06-09',NULL);
INSERT INTO "clientes" VALUES(9,'Fabio',23,'44444444444','fabio@email.com','1234-5678','Belo Horizonte','MG','2014-06-09',NULL);
INSERT INTO "clientes" VALUES(10,'Joao',21,'55555555555','joao@email.com','11-1234-5600','Sao Paulo','SP','2014-06-09',NULL);
INSERT INTO "clientes" VALUES(11,'Xavier',24,'66666666666','xavier@email.com','12-1234-5601','Campinas','SP','2014-06-10',NULL);
INSERT INTO "clientes" VALUES(12,'Matheus',22,'666','suetham@email.com','1233-3321','Tapira','CA','1988-03-15',NULL);
INSERT INTO "clientes" VALUES(13,'Regis',53,'1110110101','regis@email.com','(11) 1111-1111','Sao Paulo','SP','2016-11-13 13:33:53.217532',NULL);
INSERT INTO "clientes" VALUES(14,'Regis da Silva',35,'1234567890','regis@email.com','(11) 9876-5342','Sao Paulo','SP','2014-07-30 11:23:00.199000',NULL);
DELETE FROM "sqlite_sequence";
INSERT INTO "sqlite_sequence" VALUES('clientes',14);
COMMIT;
