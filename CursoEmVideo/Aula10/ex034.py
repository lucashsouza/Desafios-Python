sal = float(input('Digite seu salário: R$'))
if sal > 1250.00:
    sal = sal + (sal * 0.10)
else:
    sal = sal + (sal * 0.15)
print('')
print('PARABÉNS! Você ganhou um aumento!')
print('Seu novo salário é de: R${:.2f}'.format(sal))