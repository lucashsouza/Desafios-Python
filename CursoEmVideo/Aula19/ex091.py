#091 - Sorteando dados

from random import randint
from time import sleep

d = dict()

print('-' * 30)
print('{:^30}'.format('SORTEANDO DADOS'))
print('-' * 30)
print()

for c in range(1, 5):
        d[f'Jogador {c}'] = randint(1, 6)

for k, v in d.items():
        print(f'O {k} tirou um {v}')
        sleep(1)
        print()

l = list()

for i in d.items():
        l.append(i)

l.sort(key=lambda x: x[1], reverse=True)
jog = l

print('-' * 30)
print('{:^30}'.format('PLACAR'))
print('-' * 30)

for c in range(1, 5):
        print(f'{c}°Lugar = {l[c-1][0]} sorteou {l[c-1][1]}')
        sleep(1)
        print()

print('Continue brincando!','\nAperte PLAY!')
