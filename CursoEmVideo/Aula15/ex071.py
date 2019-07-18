from time import sleep

print('=' * 30)
print('{:^30}'.format('BANCO'))
print('=' * 30)
print('')
valor = int(input('Informe o valor: R$ '))
total = valor
ced = 100
totced = 0
print('')
print('Processando...')
sleep(1)
print('-' * 30)
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {totced} cédula(s) de R${ced}')
        if ced == 100:
            ced = 50
        elif ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 5
        elif ced == 5:
            ced = 1
        totced = 0
        if total == 0:
            print('-' * 30)
            break
print('')
print('Volte sempre ao BANCO. Tenha um bom dia!')
