# 093 - Aproveitamento de jogador de futebol

jogador = {}
n = str(input('Nome do Jogador: ')).strip().upper()
qnt = int(input('Quantos jogos {} participou: '.format(n))
gols = []

print('-' * 30)
print('{:^30}'.format('Aproveitamento do'))
print('{:^30}'.format(n))
print('-' * 30)
print()

for c in range(qnt):
    g = int(input('Gols de {} na partida {}: '.format(n, c+1))
    gols.append(g)
print()

jogador["nome"] = n
jogador["gols"] = gols
jogador["total"] = sum(gols)

print('-=' * 15)
print()

for c in range(qnt):
    print(' => Na partida {}, fez {} gols.'.format(c+1, jogador["gols"][c]))

print()
print('Foi um total de {} gols.'.format(jogador["total"]))
