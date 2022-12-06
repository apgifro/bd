import model.models as models


class Article:
    
    def salvar(self, id=None, titulo=None, email=None):
        try:
            if id:
                artigo = models.Artigo.get_by_id(id)
                artigo.titulo = titulo
                artigo.email = email
            else:
                artigo = models.Artigo(titulo=titulo, email=email)
            artigo.save()
            return True
        
        except Exception as e:
            print(e)
            return False
        
    def excluir(self, id):
        try:
            artigo = models.Artigo.get_by_id(id)
            artigo.delete_instance()
            return True
        except Exception as e:
            print(e)
            return False
