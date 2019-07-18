# 095 - Aproveitamento de jogadores de futebol (Ex 93 - Aprimorado)

                ''' Aprimore o desafio 093 para que ele funcione com vários jogadores,
                    incluindo um sistema de visualização de detalhes de aproveitamento
                    de cada jogador. '''

time = list()
partidas = list()
jogador = dict()

print('-' * 40)
print('{:^40}'.format('Aproveitamento dos jogadores'))
print('-' * 40)

while True:
    jogador.clear()
    jogador['nome'] = str(input('\nNome do jogador: '))
    tot = int(input('Quantas Partidas {} jogou? '.format(jogador["nome"])))
    partidas.clear()
    print()

    for c in range(0, tot):
        partidas.append(int(input('    Quantos gols na partida {}? '.format(c+1))))

    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())

    while True:
        resp = str(input('\nDeseja continuar? [S/N] ')).upper()[0]
        print()

        if resp in 'SN':
            break
        print('\nERRO! Por favor, Digite Sim ou Nao.\n')
    if resp == 'N':
        break

print('-' *40)
print('cod  ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()

print('-'*40)
for k, v in enumerate(time):
    print(f'{k:<}    ', end='')

    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-'*40)

while True:
    print('\n[999] PARAR')
    busca = int(input('Digite o cod do jogador: '))
    print()

    if busca == 999:
        break

    if busca >= len(time):
        print(f'ERRO! {busca} não é um valor válido')

    else:
        print('-='*20)
        print(f' -- Aproveitamento do {time[busca]["nome"]}: --\n ')
        for i, g in enumerate(time[busca]['gols']):
            print(f'    => Jogo {i+1}: {g} gol(s).')
        print('-='*20)
print('\n<< VOLTE SEMPRE!! >>')
