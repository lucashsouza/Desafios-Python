preco = float(input('Digite o preço do produto: R$'))
print('[1] À vista: Dinheiro/Cheque - 10% de desconto')
print('[2] À vista: Cartão - 5% de desconto')
print('[3] 2x no Cartão - Sem juros')
print('[4] 3x ou mais no Cartão - 20% de juros')
opcao = int(input('Sua opção: '))

if opcao == 1:
    preco = preco - (preco * 0.10)
    print('Valor da compra é de R${:.2f}'.format(preco))
elif opcao == 2:
    preco = preco - (preco * 0.05)
    print('Valor da compra é de R${:.2f}'.format(preco))
elif opcao == 3:
    print('Valor da compra é de R${:.2f}'.format(preco))
elif opcao == 4:
    qnt = int(input('Quantas vezes: '))
    juros = preco + (preco * 0.20)
    preco = (juros) / qnt
    print('Valor da compra é de R${:.2f}'.format(preco))
else:
    print('OPÇÃO INVÁLIDA! Tente novamente')