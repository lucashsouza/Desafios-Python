s = 0
for i in range(1, 7):
    i = int(input('Digite um número: '))
    if i % 2 == 0:
        s = s + i
print('A soma dos pares é {}'.format(s))