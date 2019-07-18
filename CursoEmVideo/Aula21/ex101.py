"""Crie um programa que tenha função voto(), cujo parametro seja o ano de
nas cimento, retornando um valor literal indicando se a pessoa tem voto
NEGADO, OPCIONAL, OBRIGATÓRIO"""


def tit():
    print('-' * 35)
    print('{:^35}'.format('Calcula VOTO'))
    print('-' * 35)
    return ''


def fim():
    from time import sleep
    sleep(3)
    return '\n*Fim de programa..*'


def voto(ano):

    from datetime import date
    atual = date.today().year
    idade = atual - ano

    if idade < 16:
        return f'\nCom {idade} anos: Não pode VOTAR.'

    elif 16 <= idade < 18 or idade >= 65:
        return f'\nCom {idade} anos, o voto é OPCIONAL.'

    else:
        return f'\nCom {idade} anos, o voto é OBRIGATÓRIO.'

# Programa Principal:


print(tit())


nasc = int(input('Ano de Nascimento: '))
print(voto(nasc))
print(fim())
