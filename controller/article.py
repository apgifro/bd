import model.models as models


class Article:
          
    def select(self):
        articles = []
        try:
            select = models.Artigo.select()
            for article in select:
                data = {"id": article.id,
                        "titulo": article.titulo,
                        "email": article.email,
                        "palavra_chave": models.PalavrasChave.get_by_id(article.id).palavra_chave,
                        "nota": models.ArtigoRevisor.get_by_id(article.id).nota}
                articles.append(data)
            return articles
        except Exception as e:
            print(e)
            return False

        
    def select_id(self,id):
        try:
            artigo = models.Artigo.get_by_id(id)
            artigo_revisor = models.ArtigoRevisor.get_by_id(id)
            palavras_chave = models.PalavrasChave.get_by_id(id)
            
            data = {"id": artigo.id,
                    "titulo": artigo.titulo,
                    "email": artigo.email,
                    "palavra_chave": palavras_chave.palavra_chave,
                    "nota": artigo_revisor.nota}
            return data
        except Exception as e:
            print(e)
            return False
    
    
    def save(self, id=None, titulo=None, email=None):
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
        
    def delete(self, id):
        try:
            artigo = models.Artigo.get_by_id(id)
            artigo.delete_instance()
            return True
        except Exception as e:
            print(e)
            return False
