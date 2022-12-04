from peewee import Model, OperationalError, CharField, IntegerField, ForeignKeyField
from playhouse.mysql_ext import MySQLConnectorDatabase


class BaseModel(Model):

    def __init__(self, *args, **kwargs):
        try:
            self.create_table()
        except OperationalError as erro:
            print(erro)

        super().__init__(*args, **kwargs)

    class Meta:
        database = MySQLConnectorDatabase(
            database='cbbd',
            user='root',
            password="",
            port="3306",
            charset="utf8mb4"
        )


class Revisor(BaseModel):

    nome = CharField(max_length=50, unique=True)
    instituicao = CharField(max_length=50, unique=True)

    rua = CharField(max_length=50, unique=True)
    numero = IntegerField()
    bairro = CharField(max_length=30, unique=True)
    cidade = CharField(max_length=50, unique=True)
    unidade_federativa = CharField(max_length=2, unique=True)


class Especialidade(BaseModel):

    nome = CharField(max_length=100, unique=True)
    revisor = ForeignKeyField(model=Revisor, on_delete="CASCADE", backref="especialidades")


class Contato(BaseModel):

    telefone = IntegerField()
    fax = IntegerField()
    revisor = ForeignKeyField(model=Revisor, on_delete="CASCADE", backref="especialidades")


class Artigo_Revisor(BaseModel):
    pass


class Artigo(BaseModel):

    titulo = CharField(max_length=100, unique=True)
    nome = CharField(max_length=100, unique=True)


class Palavras_Chave(BaseModel):
    pass


class Participante(BaseModel):
    pass


class Autor(BaseModel):
    pass


class Inscrito(BaseModel):
    pass


class Cientista(BaseModel):
    pass


class Local(BaseModel):
    pass


class Local_Atividade(BaseModel):
    pass


class Atividade(BaseModel):
    pass


class Sessao_Tecnica(BaseModel):
    pass


class Palestra(BaseModel):
    pass


class Minicurso(BaseModel):
    pass
