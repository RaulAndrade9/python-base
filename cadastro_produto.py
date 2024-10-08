#!/usr/bin/env/python3
"""Cadastro de Produto
"""
__version__ = "0.1.0"

produto = {
    "nome": "Caneta",
    "Cores": ["Azul", "Branco"],
    "preco": 3.23,
    "dimensao": {
        "altura": 12.1,
        "largura": 0.08
    },
    "em_estoque": True,
    "codigo": 45678,
    "codebar": None,

}

cliente = {
    "nome": "Raul"
}

compra = {
    "cliente": cliente,
    "produto": produto,
    "quantidade": 3,
}

total_compra = compra["quantidade"] * compra["produto"]["preco"]

print(
    f"O cliente{compra["cliente"]["nome"]}"
    f"comprou {compra["produto"]["nome"]}"
    f"E pagou o total de {total_compra}"
)