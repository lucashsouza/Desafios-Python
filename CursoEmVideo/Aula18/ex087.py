print('-' * 30)
print('{:^30}'.format('Matriz 3x3'))
print('-' * 30)
spar = mai = scol = 0
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
par = []

for i in range(0, 3):
    for j in range(0, 3):
        #Matriz começando do 1
        matriz[i][j] = int(input(f'Valor {[i + 1, j + 1]}: '))
        if matriz[i][j] % 2 ==0:
            spar += matriz[i][j]

for i in range(0, 3):
    scol += matriz[i][2]

for c in range(0, 3):
    if c == 0:
        mai = matriz[1][c]
    elif matriz[1][c] > mai:
        mai = matriz[1][c]

print('-' * 30)
print(matriz[0])
print(matriz[1])
print(matriz[2])
print('-' * 30)

print(f'Soma dos pares: {spar}')
print(f'Soma da 3 coluna {scol}')
print(f'Maior valor da 2 linha: {mai}')