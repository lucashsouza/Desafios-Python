print('-' * 30)
print('{:^30}'.format('Matriz 3x3'))
print('-' * 30)
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for i in range(0, 3):
    for j in range(0, 3):
        #Matriz começando do 1
        matriz[i][j] = int(input(f'Valor {[i + 1, j + 1]}: '))

print('-' * 30)
print(matriz[0])
print(matriz[1])
print(matriz[2])
