r = 'S'
som = quant = media = 0

print('Digite alguns numeros')
print('')

while r in 'Ss':
    n = int(input('{}° Num:  '.format(quant)))
    som += n
    quant += 1

    r = str(input('Continuar [S/N]: ')).upper().strip()[0]

    if quant == 1:
        maior = menor = n

    else:
        if n == maior:
            maior = n
        if menor > n:
            menor = n

med = som / quant
print('')
print('Você digitou {} números e a média foi {}'.format(quant, med))
print('O maior valor foi {} e o menor {}'.format(maior, menor))
