import models

# Revisor

revisor = models.Revisor()
revisor.nome = "Alexandre"
revisor.instituicao = "CBBD"
revisor.rua = "Avenida Paulista"
revisor.numero = 2030
revisor.bairro = "Setor 2"
revisor.cidade = "Ariquemes"
revisor.unidade_federativa = "RO"
revisor.save()

revisor2 = models.Revisor()
revisor2.nome = "Jacob"
revisor2.instituicao = "CBBD"
revisor2.rua = "Avenida Paulista"
revisor2.numero = 2030
revisor2.bairro = "Setor 2"
revisor2.cidade = "Ariquemes"
revisor2.unidade_federativa = "RO"
revisor2.save()

# Especialidade do Revisor

especialidade = models.Especialidade()
especialidade.nome = "Especialidade"
especialidade.revisor = revisor
especialidade.save()

especialidade2 = models.Especialidade()
especialidade2.nome = "Especialidade2"
especialidade2.revisor = revisor2
especialidade2.save()

# Contato do Revisor

contato = models.Contato()
contato.telefone = 35076489384
contato.fax = 34554678787
contato.revisor = revisor

contato2 = models.Contato()
contato2.telefone = 23454409485
contato2.fax = 39994019484
contato2.revisor = revisor2
