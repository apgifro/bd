import peewee
from playhouse.mysql_ext import MySQLConnectorDatabase


config = {
    "database": "cbbd",
    "user": "root",
    "password": "",
    "host": "127.0.0.1"
}

db = MySQLConnectorDatabase(**config)


class Base(peewee.Model):
    class Meta:
        database = db


class Revisor(Base):

    nome = peewee.CharField(max_length=50, unique=True)
    instituicao = peewee.CharField(max_length=50, unique=True)

    rua = peewee.CharField(max_length=50, unique=True)
    numero = peewee.IntegerField()
    bairro = peewee.CharField(max_length=30, unique=True)
    cidade = peewee.CharField(max_length=50, unique=True)
    unidade_federativa = peewee.CharField(max_length=2, unique=True)


class Especialidade(Base):
    nome = peewee.CharField(max_length=100, unique=True)
    revisor = peewee.ForeignKeyField(model=Revisor, on_delete="CASCADE", backref="especialidades")


class Contato(Base):
    telefone = peewee.IntegerField()
    fax = peewee.IntegerField()
    revisor = peewee.ForeignKeyField(model=Revisor, on_delete="CASCADE", backref="especialidades")


class Artigo_Revisor(Base):
    pass


class Artigo(Base):
    titulo = peewee.CharField(max_length=100, unique=True)
    nome = peewee.CharField(max_length=100, unique=True)


class Palavras_Chave(Base):
    pass


class Participante(Base):
    pass


class Autor(Base):
    pass


class Inscrito(Base):
    pass


class Cientista(Base):
    pass


class Local(Base):
    pass


class Local_Atividade(Base):
    pass


class Atividade(Base):
    pass


class Sessao_Tecnica(Base):
    pass


class Palestra(Base):
    pass


class Minicurso(Base):
    pass


db.create_tables([Revisor, Especialidade, Contato,
          Artigo_Revisor, Artigo, Palavras_Chave,
          Participante, Autor, Inscrito,
          Cientista, Local, Local_Atividade,
          Atividade, Sessao_Tecnica, Palestra, Minicurso])
