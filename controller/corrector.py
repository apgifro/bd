import model.models as models


class Corrector:

    def select(self):
        correctors = []
        try:
            select = models.Revisor.select()
            for corrector in select:
                data = {"id": corrector.id,
                        "nome": corrector.nome,
                        "instituicao": corrector.instituicao,
                        "rua": corrector.rua,
                        "numero": corrector.numero,
                        "bairro": corrector.bairro,
                        "cidade": corrector.cidade,
                        "unidade_federativa": corrector.unidade_federativa,
                        "especialidade": models.Especialidade.get_by_id(corrector.id).nome,
                        "telefone": models.Contato.get_by_id(corrector.id).telefone,
                        "fax": models.Contato.get_by_id(corrector.id).fax}
                correctors.append(data)
            return correctors
        except Exception as e:
            print(e)
            return False

    def select_id(self, id):
        try:
            corrector = models.Revisor.get_by_id(id)
            expertise = models.Especialidade.get_by_id(id)
            contact = models.Contato.get_by_id(id)

            data = {"id": corrector.id,
                    "nome": corrector.nome,
                    "instituicao": corrector.instituicao,
                    "rua": corrector.rua,
                    "numero": corrector.numero,
                    "bairro": corrector.bairro,
                    "cidade": corrector.cidade,
                    "unidade_federativa": corrector.unidade_federativa,
                    "especialidade": expertise.nome,
                    "telefone": contact.telefone,
                    "fax": contact.fax}
            return data
        except Exception as e:
            print(e)
            return False

    def save(self,
             id=None,
             nome=None,
             instituicao=None,
             rua=None,
             numero=None,
             bairro=None,
             cidade=None,
             unidade_federativa=None,
             nome_especialidade=None,
             telefone=None,
             fax=None):
        try:
            if id:
                revisor = models.Revisor.get_by_id(id)
                revisor.nome = nome
                revisor.instituicao = instituicao
                revisor.rua = rua
                revisor.numero = int(numero)
                revisor.bairro = bairro
                revisor.cidade = cidade
                revisor.unidade_federativa = unidade_federativa

                especialidade = models.Especialidade.get_by_id(id)
                especialidade.nome = nome_especialidade

                contato = models.Contato.get_by_id(id)
                contato.telefone = telefone
                contato.fax = fax
            else:
                revisor = models.Revisor(nome=nome,
                                         instituicao=instituicao,
                                         rua=rua,
                                         numero=numero,
                                         bairro=bairro,
                                         cidade=cidade,
                                         unidade_federativa=unidade_federativa)
                especialidade = models.Especialidade(nome=nome_especialidade, revisor=revisor)
                contato = models.Contato(telefone=telefone, fax=fax, revisor=revisor)
            revisor.save()
            especialidade.save()
            contato.save()
            return True

        except Exception:
            return False

    def delete(self, id):
        try:
            revisor = models.Revisor.get_by_id(id)
            revisor.delete_instance()
            return True
        except Exception as e:
            print(e)
            return False
