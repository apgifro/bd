from corrector import Corrector
from article import Article
from autor import Autor

"""
# Corrector
print("Corrector")

control = Corrector()

save = control.save(nome='Joca',
                    instituicao='IFRO',
                    rua='Vergueiro',
                    numero=4444,
                    bairro='Alto do Ipiranga',
                    cidade='São Paulo',
                    unidade_federativa='SP')
print("Save:", save)

update = control.save(id=1,
                      nome='Lucas Martins',
                      instituicao='IFRO',
                      rua='Vergueiro',
                      numero=4444,
                      bairro='Alto do Ipiranga',
                      cidade='São Paulo',
                      unidade_federativa='SP')

print("Update:", update)

select = control.select()
print("Select:", select)

delete = control.delete(1)
print("Delete:", delete)

# Artigo
print("\nArtigo")

control = Article()

save = control.salvar(titulo="Artigo Importante",
                      email="alexandre.girardello@ifro.edu.br")
print("Save:", save)

update = control.salvar(id=1,
                        titulo="Artigo Muito Importante",
                        email="alexandre.girardello@estudante.ifro.edu.br")
print("Update:", update)

delete = control.excluir(1)
print("Delete:", delete)
"""

control = Autor()

save = control.salvar(email="emailteste@ifro.edu.br",
                      nome='João Paulo', instituicao='CBBD')
print("Save:", save)