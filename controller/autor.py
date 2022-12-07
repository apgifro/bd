import model.models as models


class Autor:

    def salvar(self, id=None, email=None, nome=None, instituicao=None):
        try:
            if id:
                autor = models.Autor.get_by_id(id)
                autor.email = email
                participante = models.Participante.get_by_id(id)
                participante.nome = nome
                participante.instituicao = instituicao
            else:
                autor = models.Autor(email=email)
                participante = models.Participante(nome=nome, instituicao=instituicao)
            autor.save()
            return True
        except Exception as e:
            print(e)
            return False

    def excluir(self, id):
        try:
            autor = models.Autor.get_by_id(id)
            autor.delete_instance()
            return True
        except Exception as e:
            print(e)
            return False