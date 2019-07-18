# 092 - Aposentadoria
from datetime import datetime

print('-' * 30)
print('{:^30}'.format('Calcule sua'))
print('{:^30}'.format('APOSENTADORIA!'))
print('-' * 30)
print()

d = dict()
nome = str(input('Nome: '))
nas = int(input('Ano de nascimento: '))
atual = datetime.now()
idade = atual.year - nas
trab = int(input('Carteira de Trabalho [0 não tenho]: '))
print()

print('-' * 30)
print('{:^30}'.format('Informações:'))
print('-' * 30)

while True:
    if trab != 0:
        contr = int(input('Contratação: '))
        sala = int(input('Salário: R$'))
        d = {'Nome:': nome, 'Idade:': idade, 'CTPS:': trab,
             'Contratado:': contr, 'Salário: R$': sala,
             'Aposentadoria:': contr + 35}
        for k, v in d.items():
            print(k, v)
        break

    else:
        d = {'Nome:': nome, 'Idade:': idade, 'CTPS:': 'Não possui',
             'Aposentadoria:': idade + 35}
        for k, v in d.items():
            print(k, v)
        break
