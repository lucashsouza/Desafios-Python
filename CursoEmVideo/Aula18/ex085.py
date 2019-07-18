num = [[], []]
v = 0
print('=' * 30)
print('{:^30}'.format('Par ou impar?'))
print(' {:^30}'.format('Utilizando listas compostas'))
print('=' * 30)
print('')

for c in range(1, 8):
    v = int(input(f'{c}° Valor: '))

    if v % 2 == 0:
        num[0].append([v])

    if v % 2 != 0:
        num[1].append([v])

print('-' *30)
num[0].sort()
num[1].sort()

if num [0] == []:
    print('')
else:
    print(f'Os pares são: {num[0]}')

if num [1] == []:
    print('')
else:
    print(f'Os impares são: {num[1]}')
