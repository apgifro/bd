from peewee import ModelSelect

from model.models import Revisor

class RevisorCtrl:
    
    def salvar(self, id=None, nome=None, instituicao=None, rua=None, numero=None, bairro=None, cidade=None, unidade_federativa=None):
        try:
            if id:
                revisor = Revisor.get_by_id(id)
                revisor.nome = nome
                revisor.instituicao = instituicao
                revisor.rua = rua
                revisor.numero = numero
                revisor.bairro = bairro
                revisor.cidade = cidade
                revisor.unidade_federativa = unidade_federativa
            else:
                revisor = Revisor(nome=nome, instituicao=instituicao, rua=rua, numero=numero, bairro=bairro, cidade=cidade, unidade_federativa=unidade_federativa)
            revisor.save()
            return "Operação realizada com sucesso!!!"
        
        except Exception as e:
            print(e)
            return "Não foi possível salvar ou atualizar"
        
    def excluir(self, id):
        try:
            revisor = Revisor.get_by_id(id)
            revisor.delete_instance()
            return "Revisor excluído com sucesso!"
        except Exception as e:
            print(e)
            return "Não foi possível excluir o Revisor!"