import peewee
import mysql.connector


class BaseModel(peewee.Model):
    """
    Classe básica para criação de novas
    classes model a partir do peewee
    """

    def __init__(self, *args, **kwargs):
        try:
            self.create_table()
        except peewee.OperationalError as erro:
            print(erro)

        super().__init__(*args, **kwargs)

    class Meta:
        """
        Conecta no servidor MySQL
        Cria o banco de dados, caso não exista
        """
        name = "cbbd"
        user = "root"
        password = ""
        host = "127.0.0.1"

        database = mysql.connector.connect(
            user=user,
            password=password,
            host=host,
        )

        cursor = database.cursor()
        cursor.execute("SHOW DATABASES")
        databases = [database[0] for database in cursor]
        cursor.execute(f"CREATE DATABASE {name}") if name not in databases else False
        cursor.execute(f"USE {name}")


class Especialidade(BaseModel):
    pass


class Contato(BaseModel):
    pass


class Revisor(BaseModel):
    pass


class Artigo_Revisor(BaseModel):
    pass


class Artigo(BaseModel):
    pass


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
