dados = list()
pessoas = list()
mai = men = 0

print('=' * 30)
print('{:^30}'.format('Peso'))
print('=' * 30)
print('')

while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))

    if len(pessoas) == 0:
        mai = men = dados[1]

    else:
        if dados[1] > mai:
            mai = dados[1]

        if dados[1] < men:
            men = dados[1]

    pessoas.append(dados[:])
    dados.clear()
    resp = str(input('Continuar (S/N): ')).strip().upper()
    print('')

    if resp in 'N':
        break

print('=' * 30)
print(f'Total de pessoas: {len(pessoas)}')
print('')
print(f'O maior peso foi {mai}KG, de: ', end='')

for p in pessoas:
    if p[1] == mai:
        print(f'[{p[0]}] ', end='')

print()
print(f'O menor peso foi {men}KG, de: ', end='')

for p in pessoas:
    if p[1] == men:
        print(f'[{p[0]}] ', end='')
