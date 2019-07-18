n = 0
som = 0
c = 1
print('Digite alguns numeros')
print('Obs: Digite 999 para ver a soma')
print('')

while n != 999:
    n = int(input('{}° Num:  '.format(c)))
    if n != 999:
        som += n
    c += 1

print('')
print('A soma é {}'.format(som))
