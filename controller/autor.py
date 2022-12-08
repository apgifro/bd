import model.models as models


class Autor:
        
    def select(self):
        autores = []
        try:
            select = models.Autor.select()
            for autor in select:
                data = {"id": autor.id,
                        "email": autor.email,
                        "nome": models.Participante.get_by_id(autor.id).nome,
                        "instituicao": models.Participante.get_by_id(autor.id).instituicao}
                autores.append(data)
            return autores
        except Exception as e:
            print(e)
            return False
        
                        
    def select_id(self,id):
        try:
            autor = models.Autor.get_by_id(id)
            participante = models.Participante.get_by_id(id)
            
            data = {"id": autor.id,
                    "email": autor.email,
                    "nome": participante.nome,
                    "instituicao": participante.instituicao}
            return data
        except Exception as e:
            print(e)
            return False
                
    
    def save(self, id=None, email=None, nome=None, instituicao=None):
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
            participante.save()
            return True
        except Exception as e:
            print(e)
            return False
    
    
    def delete(self, id):
        try:
            autor = models.Autor.get_by_id(id)
            autor.delete_instance()
            return True
        except Exception as e:
            print(e)
            return False