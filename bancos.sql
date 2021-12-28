create database cadastro
default character set utf8
default collate utf8_general_ci;
use cadastro;
create table bancos(
id int not null auto_increment,
Nome_da_Instituicao varchar(80) not null,
codigo_de_compensacao int(20),
primary key(id) 
)default charset = utf8;	
SELECT * FROM cadastro.bancos;