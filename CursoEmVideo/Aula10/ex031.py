km = float(input('Qual vai ser a distância da viagem: '))
if km <= 200:
    print('O valor a ser pago é de: R${:.2f}'.format(km * 0.50))
else:
    print('O valor a ser pago é de: R${:.2f}'.format(km * 0.45))