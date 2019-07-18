# Exercicio 096 - Area do terreno

''' Faça um programa que tenha uma função chamada area(), que receba
 as dimensões de um terreno retangular (largura e comprimento) e
 mostre a area do terreno. '''

def titulo():
    print('-'*50)
    print('{:^50}'.format('AREA DO TERRENO'))
    print('{:^50}'.format('obs: em metros'))
    print('-'*50)


def area(lar, com):
    metros = lar * com
    print()
    print('A area do terreno {:.2f} x {:.2f} é de {} m².'.format(lar, com, metros))


titulo()

lar = float(input('Largura: '))
com = float(input('Comprimento: '))

area(lar, com)
print('-'*50)
