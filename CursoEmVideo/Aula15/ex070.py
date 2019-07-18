tot = 0
c = 0
print('=' * 20)
print('LOJA DO LUSKAO')
print('=' * 20)
while True:
    prod = str(input('Produto: '))
    preco = float(input('Preço: R$'))

    barato = preco
    cnt = str(input('Continuar [S/N] ')).upper().strip()
    print('')
    tot += preco

    if barato >= preco:
        tot += preco

    if 1000 < preco:
        c += 1

    if cnt == 'N':
        break

print('=' * 35)
if c >= 1:
    print(f'{c} produtos custaram mais de R$1000.00')
print(f'O preço total da compra é R${tot:.2f}')
print(f'O produto mais barato foi {barato}')
