CREATE DATABASE IF NOT EXISTS aula_jogo_02;

USE aula_jogo_02;

CREATE TABLE IF NOT EXISTS categoria(
	id INT AUTO_INCREMENT PRIMARY KEY,
	nome VARCHAR(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS criador_jogo(
	id INT AUTO_INCREMENT PRIMARY KEY,
    site TEXT,
    contato VARCHAR(11) NOT NULL,
    nome TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS jogo(
	id INT AUTO_INCREMENT PRIMARY KEY,
    titulo TEXT NOT NULL,
    valor DECIMAL(6,2) NOT NULL,
    descricao TEXT NOT NULL,
    imagem VARCHAR(255) NOT NULL,
    id_categoria INT NOT NULL,
    FOREIGN KEY (id_categoria) REFERENCES categoria(id)
);

CREATE TABLE IF NOT EXISTS jogo_criador_jogo(
	id_jogo INT,
    id_criador_jogo INT,
    PRIMARY KEY (id_jogo, id_criador_jogo),
    FOREIGN KEY (id_jogo) REFERENCES jogo(id),
    FOREIGN KEY (id_criador_jogo) REFERENCES criador_jogo(id)
);



