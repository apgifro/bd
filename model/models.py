import peewee
import mysql.connector


class BaseModel(peewee.Model):

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
