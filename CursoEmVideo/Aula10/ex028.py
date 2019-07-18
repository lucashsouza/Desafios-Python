from random import randint
n = (randint(0, 5))
print('- JOGO DA ADIVINHAÇÃO -')
print('Regras: \nAdivinhe um número entre 0 e 5')
print('')
jog = int(input('Sua tentativa: '))
print('PARABÉNS, você acertou!' if jog == n else 'MUITO RUIM, tenta de novo!')