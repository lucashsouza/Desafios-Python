maior = 0
menos = 0
c = 0
while True:
    print('-' * 10)
    nome = str(input('Nome: ')).strip().upper()
    sexo = str(input('Sexo: [M/F] ')).strip().upper()
    idade = int(input('Idade: '))
    print('-' * 10)
    cnt = str(input('Quer continuar [S/N]? ')).strip().upper()
    if sexo == 'M':
        c += 1
        if idade >= 18:
            maior += 1
    if sexo == 'F':
        if idade < 20:
            menos += 1
    if cnt == 'N':
        break

print('')
print(f'Foram registrados {c} Homem(s), sendo {maior} maior(es) de idade')
print(f'E {menos} Mulheres de 20 anos ')
