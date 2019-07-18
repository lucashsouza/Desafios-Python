"""

Crie um programa que tenha uma função ficha(), que receba dois parametros opcionais:
1. Nome de um Jogador
2. Quantos gols ele marcou

O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.

"""


def titulo():
    print('-' * 45)
    print('{:^45}'.format('Função Ficha de jogadores '))
    print('-' * 45)
    return ''


def fim():
    from time import sleep
    sleep(3)
    return '\n*Fim de programa..*'


def ficha(jog='<desconhecido>', gol=0):
    print(f'\nJogador {jog} fez {gol} gol(s) no campeonato.')


# Programa principal

print(titulo())

nome = str(input('Nome do Jogador: '))
gols = str(input('Numero de Gols: '))

if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0

if nome.strip() == '':
    ficha(gol=gols)

else:
    ficha(nome, gols)

print(fim())
