num = (int(input('1° Número: ')),
       int(input('2° Número: ')),
       int(input('3° Número: ')),
       int(input('4° Número: ')))
print(f'Você digitou: {num}')
print('')
if 9 in num:
    print(f'O número 9 apareceu {num.count(9)} vez(es) ')
else:
    print('Não foi encontrado nenhum 9!')
if 3 in num:
    print(f'O primeiro número 3 está na {num.index(3) + 1}° posição')
else:
    print('Não foi encontrado nenhum 3!')
print('Os valores pares digitados foram ', end='')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')
