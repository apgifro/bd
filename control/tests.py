from corrector import Corrector
from article import Article


# Revisor
print("Revisor")

control = Corrector()

save = control.salvar(nome='Joca',
                      instituicao='IFRO',
                      rua='Vergueiro',
                      numero=4444,
                      bairro='Alto do Ipiranga',
                      cidade='São Paulo',
                      unidade_federativa='SP')
print("Save:", save)

update = control.salvar(id=1,
                        nome='Lucas Martins',
                        instituicao='IFRO',
                        rua='Vergueiro',
                        numero=4444,
                        bairro='Alto do Ipiranga',
                        cidade='São Paulo',
                        unidade_federativa='SP')

print("Update:", update)

delete = control.excluir(1)
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
