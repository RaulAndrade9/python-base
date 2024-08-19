"""Exibe relatório de crianças por atividade

Imprimir a lista de crianças agrupadas por sala que frequentam cada uma das atividades
"""

__version__ = "0.1.1"

sala1 = ["Erik", "Maia", "Gustavo", "Manuel", "Sofia", "Joana"]
sala2 = ["Joao", "Antonio", "Carlos", "Maria", "Isolda"]
aula_ingles = ["Erik", "Maia", "Joana", "Carlos", "Antonio"]
aula_musica = ["Erik", "Carlos", "Maria"]
aula_danca = ["Gustavo", "Sofia", "Joana", "Antonio"]
atividades = [("Dança", aula_danca),
               ("Inglês", aula_ingles),
                 ("Música", aula_musica),]

#Retornar os alunos da sala 1 que tem intersecção com a atividade

for nome_atividade, atividade in atividades:
    atividade_sala1 = set(sala1) & set(atividade)
    atividade_sala2 = set(sala2) & set(atividade)


    print(f"{nome_atividade} Sala 1",atividade_sala1)
    print(f"{nome_atividade} Sala 2",atividade_sala2)
    print("-" * 30)
        
