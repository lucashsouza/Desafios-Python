"""
Modifique as funções que foram criadas no desafio 107 para
que elas aceitem um parametro a mais, informando se o valor
retornado por elas vai ser ou não formatado pela função
moeda(), desenvolvida no desafio 108.

"""
from Aula22.ex109 import moeda
from Aula22.ex109.titulo import titulo


preco = float(input("Preço: R$"))
titulo('Informações Calculadas: ')


print(f"Metade: {moeda.metade(preco, True)}")
print(f"Dobro: {moeda.dobro(preco, True)}")
print(f"10% Acréscimo: {moeda.aumentar(preco, 10, True)}")
print(f"10% Desconto: {moeda.diminuir(preco, 10, True)}")
