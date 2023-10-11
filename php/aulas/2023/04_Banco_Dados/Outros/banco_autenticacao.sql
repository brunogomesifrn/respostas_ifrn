CREATE TABLE IF NOT EXISTS usuario(
    id int not null auto_increment primary key,
    usuario varchar(50) not null,
    senha char(40) not null,
);

insert into usuario (usuario, senha) values ("bruno", "123");