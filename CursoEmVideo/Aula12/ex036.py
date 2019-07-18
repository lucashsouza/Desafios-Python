print('Empréstimo bancário para compra de uma casa')
print('')

vcasa = float(input('Informe o valor da casa: R$'))
sal = float(input('Informe o salário do comprador: R$'))
pag = int(input('Informe em quantos anos ele irá pagar: '))

prest = (vcasa /(pag * 12))

if (prest > sal * 0.30):
    print('Empréstimo NEGADO!')
else:
    print('Empréstimo APROVADO!')
    print('Mensalidade será de R${:.2f}'.format(prest))