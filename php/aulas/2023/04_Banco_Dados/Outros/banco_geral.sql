CREATE DATABASE IF NOT EXISTS aula_01;

USE aula_01;

CREATE TABLE IF NOT EXISTS projeto(
    codigo int not null auto_increment primary key,
    nome VARCHAR(500),
    data_inicio DATE,
    valor DECIMAL(8,2)
);

CREATE TABLE IF NOT EXISTS categoria(
    id int not null auto_increment primary key,
    nome VARCHAR(100)
);

CREATE TABLE IF NOT EXISTS departamento(
    id int not null auto_increment primary key,
    nome VARCHAR(100)
);

CREATE TABLE IF NOT EXISTS colaborador(
    cpf varchar(11) not null primary key,
    matricula VARCHAR(5),
    nome VARCHAR(500),
    salario DECIMAL(10,2),
    data_nascimento DATE,
    id_categoria int,
    id_departamento int,
    FOREIGN KEY (id_categoria) REFERENCES categoria(id),
    FOREIGN KEY (id_departamento) REFERENCES departamento(id)    
);


CREATE TABLE IF NOT EXISTS projeto_colaborador(
	id int NOT NULL auto_increment PRIMARY KEY,
	cpf_colaborador varchar(11) NOT NULL,
	codigo_projeto int NOT NULL,
	FOREIGN KEY (cpf_colaborador) REFERENCES colaborador(cpf),
    FOREIGN KEY (codigo_projeto) REFERENCES projeto(codigo)
);