"""
Insere e-mails em um arquivo para serem lidos posteriormentes
"""

import os
continua = 1
path = os.curdir
filepath = os.path.join(path, 'listaemail.txt')
lista = []


insere_email = int(input("Deseja inserir um e-mail ?"))
if insere_email == 1:
    while(continua == 1):
        nome = input("Informe o nome: ")
        email = input("Informe o e-mail: ")
        
        with open(filepath, 'a') as arquivo:
            arquivo.write(nome)
            arquivo.write(', ')
            arquivo.write(email)
            arquivo.write('\n')

        continua = int(input("Deseja continuar ?"))


with open(filepath, 'r') as arquivo:
        for linha in arquivo:
             nome_email = linha.split(", ")
             lista.append(nome_email)
             print(f"O nome é: {nome_email[0]}\nO e-mail é: {nome_email[1]}")
        


