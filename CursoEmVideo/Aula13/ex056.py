sidade = 0
maior = 0
nvelho = ''
totmulher = 0
for p in range(1, 5):
    print('=' * 10)
    print('{} Pessoa: '.format(p))

    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo (M/F): ')).strip().upper()
    sidade += idade
    print('')
if p == 1 and sexo == ('M'):
    maior = idade
    nvelho = nome
if sexo == ('M') and idade > maior:
    maior = idade
    nvelho = nome
if sexo == ('F') and idade < 20:
    totmulher += +1
media = sidade / 4
print('A média da idade é {} anos'.format(media))
print('O homem mais velho tem {} é o {}'.format(idade, nvelho))
print('Ao todo são {} Mulher(es) menores de 20 anos.'.format(totmulher))