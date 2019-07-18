s = 0
print('Numeros impares e multiplos de 3 entre 1 à 500')
for i in range(1, 501, 2):
    if i % 3 == 0:
        s = s + i
print('A soma requisitada é {}'.format(s))