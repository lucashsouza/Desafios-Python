"""
Adapte o código do desafio 107, criando uma função
adicional chamada moeda() que consiga mostrar os
valores como um valor monetário formatado.

"""
from Aula22.ex108 import moeda
from Aula22.ex108.titulo import titulo


preco = float(input("Preço: R$"))
titulo('Informações Calculadas: ')


print(f"Metade: {moeda.moeda(moeda.metade(preco))}")
print(f"Dobro: {moeda.moeda(moeda.dobro(preco))}")
print(f"10% Acréscimo: {moeda.moeda(moeda.aumentar(preco, 10))}")
print(f"10% Desconto: {moeda.moeda(moeda.diminuir(preco, 10))}")
