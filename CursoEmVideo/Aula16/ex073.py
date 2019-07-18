print('=' * 30)
print('{:^30}'.format('BRASILEIRÃO 2018'))
print('{:^30}'.format('17° Rodada'))
print('=' * 30)
chape = 'Chapecoense'
brasil = ('São Paulo', 'Flamengo', 'Grêmio', 'Internacional', 'Atlético',
         'Palmeiras', 'Corinthians', 'Cruzeiro', 'Fluminense',
         'América-MG', 'Botafogo', 'Vasco da Gama', 'Sport Recife',
         'EC Vitória', 'Santos', 'Bahia', 'Chapecoense', 'Atético-PR',
         'Ceará SC', 'Paraná')
print('')
print('[1] TOP 5')
print('[2] REBAIXAMENTO')
print('[3] ALFABÉTICA')
print('[4] CHAPECOENSE')
print('[5] SAIR DO PROGRAMA')
print('')
while True:
    print('')
    opcao = int(input('Sua opção: '))
    if opcao == 1:
        print('')
        print('-' * 30)
        print('{:^30}'.format('TOP 5'))
        print('-' * 30)
        for pos in range(0, 5):
            print(f'{pos + 1}° Lugar: {brasil[pos]}')
    elif opcao == 2:
        print('')
        print('-' * 30)
        print('{:^30}'.format('REBAIXAMENTO'))
        print('-' * 30)
        for pos in range(16, 20):
            print(f'{pos + 1}° Lugar: {brasil[pos]}')
    elif opcao == 3: #Fazer lista depois
        print('')
        print('-' * 30)
        print('{:^30}'.format('LISTA DOS TIMES'))
        print('{:^30}'.format('em ordem alfabética'))
        print('-' * 30)
        print(sorted(brasil))
    elif opcao == 4:
        print('')
        print('-' * 30)
        print('{:^30}'.format('CHAPECOENSE: '))
        print('-' * 30)
        print(f'{brasil.index(chape) + 1}° Lugar: CHAPECOENSE')
    elif opcao == 5:
        print('Volte sempre!\nFinalizando..')
        break
    else:
        print('OPÇÃO INVÁLIDA. Tente novamente!')
