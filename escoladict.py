"""Exibe relatório de crianças por atividade usando dicionário

Imprimir a lista de crianças agrupadas por sala que frequentam cada uma das atividades
"""

__version__ = "0.1.1"

sala1 = ["Erik", "Maia", "Gustavo", "Manuel", "Sofia", "Joana"]
sala2 = ["Joao", "Antonio", "Carlos", "Maria", "Isolda"]
aula_ingles = ["Erik", "Maia", "Joana", "Carlos", "Antonio"]
aula_musica = ["Erik", "Carlos", "Maria"]
aula_danca = ["Gustavo", "Sofia", "Joana", "Antonio"]

atividades = {"Dança": aula_danca, "Inglês": aula_ingles, "Música": aula_musica}

#Retornar os alunos da sala 1 que tem intersecção com a atividade

for key, value in atividades.items():
    atividade_sala1 = set(sala1) & set(value)
    atividade_sala2 = set(sala2) & set(value)

    print(f"Alunos da Sala 1 que estão na atividade {key}: {atividade_sala1}")
    print(f"Alunos da Sala 2 que estão na atividade {key}: {atividade_sala2}")

   
