vel = float(input('Velocidade atual do carro: '))
if vel > 80:
    multa = vel - 80
    print('Multado em R${:.2f}'.format(multa * 7))
print('Tenha um bom dia! Dirija com segurança')