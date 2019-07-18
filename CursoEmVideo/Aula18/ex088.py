from random import randint
from time import sleep

lista = list()
jogos = list()
tot = 1

print('-=' * 16)
print('{:^30}'.format('MEGA SENA'))
print('-=' * 16)

print()
n = int(input('Quantidade de apostas: '))
print()

while tot <= n:
    c = 0
    while True:
        num = randint(1, 60)

        if num not in lista:
            lista.append(num)
            c += 1

        if c >= 6:
            break

    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1

print('-=' * 3, f'Sorteando {n} JOGOS ', '-=' * 3)
print()

for i, l in enumerate(jogos):
    print(f'Jogo {i + 1}: {l} ')
    sleep(2)
    print()
print('-=' * 4, '< BOA SORTE! >', '-=' * 4)
