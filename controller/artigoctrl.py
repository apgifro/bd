from peewee import ModelSelect

from model.models import Artigo

class ArtigoCtrl:
    
    def salvar(self, id=None, titulo=None, email=None):
        try:
            if id:
                artigo = Artigo.get_by_id(id)
                artigo.titulo = titulo
                artigo.email = email
            else:
                artigo = Artigo(titulo=titulo,email=email)
            artigo.save()
            return "Operação realizada com sucesso!!!"
        
        except Exception as e:
            print(e)
            return "Não foi possível salvar ou atualizar"
        
    def excluir(self,id):
        try:
            artigo = Artigo.get_by_id(id)
            artigo.delete_instance()
            return "Artigo excluído com sucesso!"
        except Exception as e:
            print(e)
            return "Não foi possível excluir o Artigo!"