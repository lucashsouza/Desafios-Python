"""
Crie um módulo chamado moeda.py que tenha as funções
incorporadas: aumentar(), diminuir(), dobro() e metade().

Faça também um programa que importe esse módulo e use algumas dessas funções.

"""
from Aula22.ex107 import moeda
from Aula22.ex107.titulo import titulo


preco = float(input("Preço: R$"))
titulo('Informações Calculadas: ')


print(f"A metade de R${preco} é R$ {moeda.metade(preco)}")
print(f"O dobro de {preco} é R${moeda.dobro(preco)}")
print(f"Aumentando 10%, temos R${moeda.aumentar(preco, 10)}")
print(f"10% de desconto: R${moeda.diminuir(preco, 10)}")
