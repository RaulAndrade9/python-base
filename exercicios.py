produto = {
    "nome": "Caneta",
    "cor": ["azul", "branco", "vermelho"],
    "preco": 2.50,
    "dimensao_altura": 10.8,
    "dimensao_largura": 0.7,
    "em_estoque": True,
    "codigo": 454545,
}

teste = {
    "A": 'a'
}

produto.update(teste)

for key in produto:
    print(key, "-->", produto[key])


