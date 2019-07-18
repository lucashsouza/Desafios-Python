#tabuada
tab = int(input('Qual Tabuada? '))
for i in range(1, 11):
    print('{} x {}'.format(tab, i), ('= {}'.format(tab * i)))