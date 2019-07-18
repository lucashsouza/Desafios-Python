lista = []
impar = []
par = []
c = 1

print('=' * 30)
print('{:^30}'.format('Lista Par/Impar '))
print('=' * 30)
print('')

while True:
    n = (int(input(f'{c}° Valor: ')))
    resp = str(input('Continuar (S/N): ')).strip().upper()
    print('')

    if resp == 'S':
        lista.append(n)
        c += 1

        if n % 2 == 0:
            par.append(n)

        elif n % 2 != 0:
            impar.append(n)

    else:
        lista.append(n)

        if n % 2 == 0:
            par.append(n)

        elif n % 2 != 0:
            impar.append(n)
        break

print('=' * 30)
print(f'Lista completa: {lista}')

if len(par) == 0:
    print('')

else:
    print(f'Pares: {par}')

if len(impar) == 0:
    print('')

else:
    print(f'Impares: {impar}')
print('=' * 30)
