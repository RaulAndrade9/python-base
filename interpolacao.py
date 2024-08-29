
import os
import sys

arguments = sys.argv[1:]
filename = arguments[0]
templatename = arguments[1]

path = os.curdir
filepath = os.path.join(path, filename)
templatepath = os.path.join(path, templatename)
if not arguments:
    print("informe o nome do arquivo de emails")
    sys.exit(1)


clientes = []
for linha in open(filepath, encoding="utf-8"):
    nome, email = linha.split(",")

    print(f"Enviando email para : {email}")
    print()
    print(
        open(templatepath, encoding="utf-8").read()
        %{
            "nome": nome,
            "produto": "caneta",
            "texto": "Escrever muito bem",
            "link": "http://canetaslegais.com",
            "quantidade": 1,
            "preco": 50.5,
            
        }
    )
    print("-" *50)
