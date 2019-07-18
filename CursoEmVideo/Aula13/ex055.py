#pesos
maior = 0
menor = 100000
for p in range(1, 6):
    peso = float(input('{}° peso: '.format(p)))
    if peso > maior:
            maior = peso
    if peso < menor:
            menor = peso

print('Processando..')
print('O maior peso lido foi de {}KG '.format(maior))
print('O menor peso lido foi de {}KG '.format(menor))