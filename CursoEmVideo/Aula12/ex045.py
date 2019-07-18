from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('\033[1;33mJOKENPO')

print('''\033[1;31mRegras:
\033[1m1° A pedra vence a tesoura
2° O papel vence a pedra
3° A tesoura vence o papel''')

print('')

print('''\033[1;31mSuas opções:
\033[m\033[1m[0] para Pedra
[1] para Papel
[2] para Tesoura''')
jog = int(input('\033[1;33mQual é a sua jogada? '))

print('')

print('\033[1;31mJO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!\033[m')
print('')

print('-=' * 11)
print('\033[1;34mComputador jogou {}'.format(itens[computador]))
print('Jogador jogou {}\033[m'.format(itens[jog]))
print('-=' * 11)

print('')
print('\033[1;31;mRESULTADO:')

if computador == 0:
    if jog == 0:
        print('EMPATE')
    elif jog == 1:
        print('JOGADOR GANHOU')
    elif jog == 2:
        print('COMPUTADOR GANHOU')
    else:
        print('JOGADA INVÁLIDA')

elif computador == 1:
        if jog == 0:
            print('COMPUTADOR GANHOU')
        elif jog == 1:
            print('EMPATE')
        elif jog == 2:
            print('JOGADOR GANHOU')
        else:
            print('JOGADA INVÁLIDA!')

elif computador == 2:
        if jog == 0:
            print('JOGADOR GANHOU')
        elif jog == 1:
            print('COMPUTADOR GANHOU')
        elif jog == 2:
            print('EMPATE')
        else:
            print('JOGADA INVÁLIDA!')
