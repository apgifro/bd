import model.models as models


class Corrector:

    def select(self):
        correctors = []
        try:
            select = models.Revisor.select()
            for corrector in select:
                correctors.append({"id": corrector.id,
                                   "nome": corrector.nome,
                                   "instituicao": corrector.instituicao,
                                   "rua": corrector.rua,
                                   "numero": corrector.numero,
                                   "bairro": corrector.bairro,
                                   "cidade": corrector.cidade})
            return correctors
        except Exception:
            return False
    
    def save(self,
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
        
        except Exception:
            return False
        
    def delete(self, id):
        try:
            revisor = models.Revisor.get_by_id(id)
            revisor.delete_instance()
            return True
        except Exception:
            return False
