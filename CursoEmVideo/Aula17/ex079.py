valores = []
c = 1
continuar = 'S'
while continuar != 'N':
    valor = int(input(f'{c} Número: '))
    if valor not in valores:
        valores.append(valor)
        print('Valor adicionado com sucesso!')
        c += 1
        print(' ')
    else:
        print('Erro! Valor duplicado.')
        print('')
    continuar = input('Deseja continuar? [S/N] ').upper()
    print('')
valores.sort()
print('-' * 30)
print(f'Os valores digitados foi: {valores}')
