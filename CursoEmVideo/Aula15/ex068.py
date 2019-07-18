from random import randint
from time import sleep

opcao = 0
s = 0
par = 0
impar = 1
vit = 0
print('-' * 20, '\nPAR OU ÍMPAR')
print('-' * 20)

while True:
    n = int(input('Digite um numero: '))
    pc = randint(0, 10)

    s = n + pc

    if s % 2 == 0:
        res = par
    else:
        res = impar

    print('')
    print('[0] PAR\n[1]ÍMPAR')
    print('')
    opcao = int(input('Opção: '))



    if opcao == 0:
        print('-'* 20)
        print('Jogador escolheu PAR')
        print('Computador escolheu ÍMPAR')

        print('')
        print('\033[1;31mPAR')
        sleep(2)
        print('OU')
        sleep(1)
        print('ÍMPAR!!!\033[m')
        print('')

        if res == par:
            print('Jogador Venceu!')
            print('')
            vit += 1

        else:
            print('Computador Venceu!')
            print('')
            break

    elif opcao == 1:
        print('Jogador escolheu ÍMPAR')
        print('Computador escolheu PAR')

        print('')
        print('\033[1;31mPAR')
        sleep(2)
        print('OU')
        sleep(1)
        print('ÍMPAR!!!\033[m')
        print('')
        if res == impar:
            print('Jogador Venceu!')
            vit += 1
            print('')

        else:
            print('Computador Venceu!')
            print('')
            break

    else:
        print('JOGADA INVÁLIDA!')
        print('')

print('GAME OVER!')
print(f'Você venceu {vit} vez(es)')
