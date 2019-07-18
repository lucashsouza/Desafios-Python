# Exercicio 100 - Sortear numeros

''' Faça um programa que tenha uma lista chamada números e duas funções chamadas
    sorteia() e somapar(). A primeira função vai sortear 5 numeros e vai
    coloca-los dentro da lista e a segunda função vai mostrar a soma entre todos
    os valores PARES sorteados na função anterior. '''

from random import randint
from time import sleep

numeros = list()


def tit():
    print('-' * 45)
    print('{:^45}'.format('Sorteando numeros'))
    print('-' * 45)
    print()


def sorteia():
    print('Aguarde..')
    for c in range(0, 5):
        numeros.append(randint(1, 10))
    sleep(1)
    print(f'\nNumeros sorteados: {numeros}')


def somapares():
    soma = 0
    for c in numeros:
        if c % 2 == 0:
            soma += c
    print(f'Soma dos pares: {soma}')


tit()
sorteia()
somapares()
