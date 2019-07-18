# Exercicio 099 - Maior

''' Faça um programa que tenha uma função maior(), que receba
    vários parâmetros com valores inteiros.

    Seu programa tem que analisar todos os valores
    e dizer que deles é o maior. '''


def lin():
    print('-' * 35)


def tit():
    print('-' * 35)
    print('{:^35}'.format('MAIOR'))
    print('-' * 35)


def maior(* valores):
    print('Valores informados:')
    for n in valores:
        print(n, end=' ')
    print('')
    lin()
    print('{:^40}'.format('-- Analisando: --\n'))
    print(f'* Foram informados {len(valores)} números ao todo.\n')
    print(f'* O maior valor informado foi {max(valores)}.')
    lin()


tit()
maior(1, 2, 3, 4, 5) 
