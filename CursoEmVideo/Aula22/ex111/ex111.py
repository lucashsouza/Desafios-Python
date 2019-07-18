"""
Crie um pacote chamado utilidades que tenha dois módulos internos
chamados moeda e dado.

Transfira todas as funções utilizadas nos desafios 107, 108 e 109
para o primeiro pacote e mantenha tudo funcionando.

"""
from Aula22.ex111.utilidades import moeda

preco = float(input("Preço: R$"))

moeda.resumo(preco, 80, 20)
