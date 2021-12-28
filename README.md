# API-REST-Flask-MySQL
> Status: Developing⚠️
> 
Este projeto foi elaborado com a finalidade de construir uma API que realizasse as seguintes funções: 

1 - Criar uma tabela no banco de dados MySQL e armazenar a lista de bancos, presente no arquivo em anexo. 

2 - Criar uma api utilizando um framework web da sua escolha, para disponibilizar as informações presentes no banco de dados que você criou, com os seguintes endpoints: 

2.1 - Listagem de todos os bancos - método GET;

2.2 - Consultar um banco passando o código de compensação como parâmetro - método GET;


# Mas afinal, como funciona?

1- Abrindo o Postman web e digitando o URL  http://127.0.0.1:5000/bancos/ obtemos como resultado a Listagem de todos os bancos através do método GET
![Part1 upload  escale](https://github.com/victorcarv16/assets/blob/main/1.PNG)


2- Modificar a URL para  http://127.0.0.1:5000/bancos/codigo  utilizar a aba BODY e selecionar as opções ROW no formato JSON.
2.1 - Após a etapa 2 selecione digite o código da instituição financeira desejada no campo de texto e pressione SEND
![Part1 upload  escale](https://github.com/victorcarv16/assets/blob/main/2.PNG)
