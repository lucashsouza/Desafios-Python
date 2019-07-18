#maioridade
maior = 0
menor = 0
from datetime import date
atual = date.today().year
for p in range(1, 7):
    print('Em que ano a {}° Pessoa nasceu? '.format(p))
    ano = int(input('Ano de nascimento: '))
    if (atual - ano) >= 21:
        maior += 1
    else:
        menor += 1

print('Maiores de idade: {}'.format(maior))
print('Menores de idade: {}'.format(menor))