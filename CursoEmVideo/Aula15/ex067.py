'''n = int(input('Qual tabuada? '))
for c in range(0, 11):
    print(f'{n} x {c} = {n * c}')'''

n = 1
c = 0
while True:
    n = int(input('Qual tabuada? '))
    print('-' * 30)
    if n < 0:
        break
    for c in range(0, 11):
        print(f'{n} x {c} = {n * c}')
    print('-' * 30)

    c += 1
print('Programa finalizado, volte sempre! ')