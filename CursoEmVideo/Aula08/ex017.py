from math import hypot
co = float(input('Comprimento do Cateto oposto: '))
ca = float(input('Comprimento do Cateto adjacente: '))
hi= hypot(co, ca)
print('A hipotenusa mede {:.2f}'.format(hi))