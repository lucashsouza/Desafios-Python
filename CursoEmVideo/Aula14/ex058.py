from random import randint
c = 1
n = (randint(0, 11))
print('- JOGO DA ADIVINHAÇÃO -')
print('Adivinhe um número entre 0 e 10')
jog = int(input('1° tentativa: '))
print('')
while jog != n:
    jog = int(input('Errou! Tente novamente: '))
    c += 1
    if jog == n:
        print('Parabens, você acertou em {} tentativas'.format(c))