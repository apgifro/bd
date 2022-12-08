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
    nome = peewee.CharField(max_length=50)
    instituicao = peewee.CharField(max_length=50)

    rua = peewee.CharField(max_length=50)
    numero = peewee.IntegerField()
    bairro = peewee.CharField(max_length=30)
    cidade = peewee.CharField(max_length=50)
    unidade_federativa = peewee.CharField(max_length=2)


class Especialidade(Base):
    nome = peewee.CharField(max_length=100)
    revisor = peewee.ForeignKeyField(model=Revisor, on_delete="CASCADE", backref="especialidades")


class Contato(Base):
    telefone = peewee.IntegerField()
    fax = peewee.IntegerField()
    revisor = peewee.ForeignKeyField(model=Revisor, on_delete="CASCADE", backref="especialidades")


class Artigo(Base):
    titulo = peewee.CharField(max_length=100, unique=True)
    email = peewee.CharField(max_length=50)


class ArtigoRevisor(Base):
    artigo = peewee.ForeignKeyField(model=Artigo, on_delete="CASCADE", backref="artigos")
    revisor = peewee.ForeignKeyField(model=Revisor, on_delete="CASCADE", backref="revisores")
    nota = peewee.IntegerField()


class PalavrasChave(Base):
    artigo = peewee.ForeignKeyField(model=Artigo, on_delete="CASCADE", backref="artigos")
    palavra_chave = peewee.CharField(max_length=30)


class Participante(Base):
    nome = peewee.CharField(max_length=50)
    instituicao = peewee.CharField(max_length=100)


should = False
class Autor(Base):
    email = peewee.CharField(max_length=50)
    participante = peewee.ForeignKeyField(model=Participante, on_delete="CASCADE", backref="participantes")
    if should:
        artigo = peewee.ForeignKeyField(model=Artigo, on_delete="CASCADE", backref="artigos")


class ArtigoAutor(Base):
    artigo = peewee.ForeignKeyField(model=Artigo, on_delete="CASCADE", backref="artigos")
    autor = peewee.ForeignKeyField(model=Autor, on_delete="CASCADE", backref="autores")


class Inscrito(Base):
    participante = peewee.ForeignKeyField(model=Participante, on_delete="CASCADE", backref="participantes")
    categoria = peewee.CharField(max_length=100)
    email = peewee.CharField(max_length=50)
    endereco = peewee.CharField(max_length=150)
    telefone = peewee.IntegerField()


class Cientista(Base):
    participante = peewee.ForeignKeyField(model=Participante, on_delete="CASCADE", backref="participantes")
    codigo_voo = peewee.CharField(max_length=20)
    companhia_voo = peewee.CharField(max_length=30)
    data_voo_ida = peewee.DateField()
    data_voo_volta = peewee.DateField()
    hora_voo_ida = peewee.TimeField()
    hora_voo_volta = peewee.TimeField()


class Local(Base):
    nome = peewee.CharField(max_length=40)
    capacidade = peewee.IntegerField()


class Atividade(Base):
    data = peewee.DateField()
    horario = peewee.TimeField()


class LocalAtividade(Base):
    local = peewee.ForeignKeyField(model=Local, on_delete="CASCADE", backref="locais")
    atividade = peewee.ForeignKeyField(model=Atividade, on_delete="CASCADE", backref="atividades")


class SessaoTecnica(Base):
    atividade = peewee.ForeignKeyField(model=Atividade, on_delete="CASCADE", backref="atividades")
    titulo = peewee.CharField(max_length=50)
    descricao = peewee.CharField(max_length=300)
    artigo = peewee.ForeignKeyField(model=Artigo, on_delete="CASCADE", backref="artigos")


class Palestra(Base):
    atividade = peewee.ForeignKeyField(model=Atividade, on_delete="CASCADE", backref="atividades")
    titulo = peewee.CharField(max_length=50)
    participante = peewee.ForeignKeyField(model=Participante, on_delete="CASCADE", backref="participantes")


class Minicurso(Base):
    atividade = peewee.ForeignKeyField(model=Atividade, on_delete="CASCADE", backref="atividades")
    titulo = peewee.CharField(max_length=50)
    descricao = peewee.CharField(max_length=300)
    taxa = peewee.FloatField()
    vagas_disponiveis = peewee.IntegerField()
    participante = peewee.ForeignKeyField(model=Participante, on_delete="CASCADE", backref="participantes")


db.create_tables([Revisor, Especialidade, Contato,
          ArtigoRevisor, Artigo, PalavrasChave,
          Participante, Autor, ArtigoAutor, Inscrito,
          Cientista, Local, LocalAtividade,
          Atividade, SessaoTecnica, Palestra, Minicurso])
