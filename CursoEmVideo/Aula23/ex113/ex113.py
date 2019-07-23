"""

Reescreva a função leiaInt() que fizemos no desafio 104,
incluindo agora a possibilidade da digitação de um
número de tipo inválido.

Aproveite e crie também uma função leiaFloat() com a
mesma funcionalidade.

"""

from Aula23.ex113 import uteis

uteis.titulo("Função para Ler apenas números INTEIRO. ")
inteiro = uteis.leiaInt('Digite um Inteiro: ')

uteis.titulo("Função para Ler apenas números REAIS. ")
real = uteis.leiaFloat('Digite um Real: ')

print(uteis.resultados(inteiro, real))
