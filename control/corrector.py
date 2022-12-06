import model.models as models


class Corrector:
    
    def salvar(self,
               id=None,
               nome=None,
               instituicao=None,
               rua=None,
               numero=None,
               bairro=None,
               cidade=None,
               unidade_federativa=None):
        try:
            if id:
                revisor = models.Revisor.get_by_id(id)
                revisor.nome = nome
                revisor.instituicao = instituicao
                revisor.rua = rua
                revisor.numero = numero
                revisor.bairro = bairro
                revisor.cidade = cidade
                revisor.unidade_federativa = unidade_federativa
            else:
                revisor = models.Revisor(nome=nome,
                                  instituicao=instituicao,
                                  rua=rua,
                                  numero=numero,
                                  bairro=bairro,
                                  cidade=cidade,
                                  unidade_federativa=unidade_federativa)
            revisor.save()
            return True
        
        except Exception as e:
            print(e)
            return False
        
    def excluir(self, id):
        try:
            revisor = models.Revisor.get_by_id(id)
            revisor.delete_instance()
            return True
        except Exception as e:
            print(e)
            return False
