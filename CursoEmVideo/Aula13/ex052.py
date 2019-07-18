#numeros primos
tot = 0
n = int(input('Digite um numero: '))
for c in range(1, n + 1):
    if n % c == 0:
        print('\033[32m', end='')
        tot += 1
    else:
        print('\033[37m',  end='')
    print('{} '.format(c), end='')
print('\n\033[mO número {} foi divisível {} vezes '.format(n, tot))
if tot == 2 or tot == 1:
    print('É um número PRIMO!')
else:
    print('Não é um número primo')
