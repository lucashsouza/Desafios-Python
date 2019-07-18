from math import sin, cos, tan, radians
ang = float(input('Angulo: '))
seno = sin(radians(ang))
cos = cos(radians(ang))
tan = tan(radians(ang))
print('O angulo de {}° tem o SENO de {:.2f}'.format(ang, seno))
print('o COSSENO de {:.2f}\ne TANGENTE de {:.2f}'.format(cos, tan))