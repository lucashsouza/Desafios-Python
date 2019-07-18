'''
from math import factorial
cnt = 0
while cnt == 0:
    print('')
    num = int(input('Fatorial: '))
    f = factorial(num)
    print('O fatorial do número {} é {}'.format(num, f))
    print('')
    print(' [0] Continuar\n [1] Sair')
    print('')
    cnt = int(input('Opção: '))
'''

n = int(input('Digite um número para calcular o seu fatorial: '))
c = n
f = 1
print('Calculando {}!'.format(n))
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f))
