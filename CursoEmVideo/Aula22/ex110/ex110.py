"""
Modifique as funções que foram criadas no desafio 107 para
que elas aceitem um parametro a mais, informando se o valor
retornado por elas vai ser ou não formatado pela função
moeda(), desenvolvida no desafio 108.

"""
from Aula22.ex110 import moeda

preco = float(input("Preço: R$"))

moeda.resumo(preco)
