import os

mensagem = input('Insira um texto ')

path = os.path.join(os.curdir, 'arquivos')
filepath = os.path.join(path, 'arquivo.txt')


os.makedirs(path, exist_ok=True)
arquivo = open(filepath, 'a', encoding='UTF-8')

arquivo.write(mensagem)
arquivo.write('\n')
arquivo.close()

arquivo = open(filepath, 'r', encoding='UTF-8')
print(arquivo.read())