#ordenando uma lista sem 'short()'

print('=' * 30)
print('{:^30}'.format('Ordenando uma lista'))
print('{:^30}'.format('Obs: Não repita valores!'))
print('=' * 30)
print('')

lista = []

for c in range(0, 5):
    n = int(input(f'{c + 1}° Num: '))

    if c == 0 or n > lista[len(lista)-1]:
        lista.append(n)
        print('Adicionado ao final da lista...')
        print('')

    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Valor adicionado na posição {pos}')
                print('')
                pos += 1
                break

print('')
print('=' * 42)
print(f'A lista digitada foi: {lista}')
