# Exercicio 098 - Contador com parâmetros

''' Faça um programa que tenha uma função chamada contador() que receba
    três parêmetros: inicio, fim e passo
    E realize a contagem.

    Seu programa tem que realizar três contagens através da função criada:

    a) De 1 até 10, de 1 em 1
    b) De 10 até 0, de 2 em 2
    c) Uma contagem personalizada '''

def titulo():
    print('CONTADOR COM PARÂMETROS\n')

def contador(inicio, fim, passo):
    if passo <= 0:
        passo *= -1
        if passo == 0:
            print("Não é possivel usar 0 no passo.")
            return
    if fim < inicio:
        passo *= -1

    for i in range(inicio, fim, passo):
        print(i, end=' ')
    print()

titulo()
print('Contador A: '), contador(1, 10 + 1, 1)
print('Contador B: '), contador(10, 0 - 1, -2)

print('\n* Contador personalizado *\n')
inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))

if fim < inicio:
    passo *= -1
    print('Contador C: '), contador(inicio, fim-1, passo)
else:
    print('Contador C: '), contador(inicio, fim+1, passo)
