"""Exibe relatório de crianças por atividade

Imprimir a lista de crianças agrupadas por sala que frequentam cada uma das atividades
"""

__version__ = "0.1.0"

sala1 = ["Erik", "Maia", "Gustavo", "Manuel", "Sofia", "Joana"]
sala2 = ["Joao", "Antonio", "Carlos", "Maria", "Isolda"]
aula_ingles = ["Erik", "Maia", "Joana", "Carlos", "Antonio"]
aula_musica = ["Erik", "Carlos", "Maria"]
aula_danca = ["Gustavo", "Sofia", "Joana", "Antonio"]
atividades = [("Dança", aula_danca),
               ("Inglês", aula_ingles),
                 ("Música", aula_musica),]

#listar alunos em cada atividade por sala

for nome_atividade, atividade in atividades:
    atividade_sala1 = []
    atividade_sala2 = []

    for aluno in atividade:
        if aluno in sala1:
            atividade_sala1.append(aluno)
        elif aluno in sala2:
            atividade_sala2.append(aluno)

    print(f"{nome_atividade} Sala 1",atividade_sala1)
    print(f"{nome_atividade} Sala 2",atividade_sala2)
    print("-" * 30)
        
