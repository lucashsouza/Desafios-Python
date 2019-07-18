c = ('Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez',
     'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete',
     'Dezoito', 'Dezenove', 'Vinte')
print(c)
n = int(input('Digite um numero de 1 a 20: '))
if n > 20 or n < 0:
    print('Tente novamente. Digite um numero de 1 a 20: ')
else:
    print(f'Você digitou: {c[n - 1]}')
