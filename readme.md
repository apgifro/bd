# CBBD

Discentes: Alexandre e Jacob.

Disciplina: Programação II e Banco de Dados.

## Modelo Conceitual

![modelo_conceitual](/base/conceitual/CBBD-F.png)

## Modelo Lógico

![modelo_logico](/base/logico/CBBD-L-F.png)

## Modelo Físico

Clique [aqui](/base/fisico/sql.txt) para ver o SQL.

Criado pelo Peewee.

## Capturas de Tela

![screen](/base/telas/1.png)

![screen](/base/telas/2.png)

![screen](/base/telas/3.png)

![screen](/base/telas/4.png)

![screen](/base/telas/5.png)


## Montar o ambiente

1. Abra o PyCharm
2. Clique em _Get from VCS_
3. Adicione o link do projeto do GitHub
```
https://github.com/apgifro/bd
```
4. Clone o projeto
5. Configure o interpretador e _venv_
6. Instale as bibliotecas
```
pip install kivy kivymd peewee mysql-connector-python
```
Alternativamente, a biblioteca seguinte poderá ser necessária:
```
pip install mysql-connector
```

7. Instale e inicie o MySQL 
8. Faça login no banco de dados
```
mysql -u root
```
9. Crie uma base de dados
```
create database cbbd;
```

10. Execute o arquivo `main.py` no diretório raiz