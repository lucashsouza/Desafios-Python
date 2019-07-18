print('=' * 30)
print('{:^30}'.format('Lista'))
print('=' * 30)
print('')

lista = []
c = 1

while True:
    n = int(input(f'{c}° Valor: '))
    resp = str(input('Continuar (S/N): ')).upper().strip()
    print('')
    lista.append(n)

    if resp == 'S':
        c += 1

    else:
        print('=' * 30)
        print('{:^30}'.format('Analisando a lista'))
        print('=' * 30)
        break

print('')
print(f'Foram digitados: {len(lista)} número(s).')
print('')

lista.sort(reverse=True)
print(f'Decrescente: {lista}')
print('')

if 5 in lista:
    print('O número 5 está na lista')
else:
    print('O número 5 não está na lista')

print('')
print(f'Lista completa (ordem que foi digitada):\n{lista}')
