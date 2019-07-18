print('=' * 10, '10 TERMOS DE UMA PA', '=' * 10)
t1 = int(input('Primeiro termo: '))
r = int(input('Razão: '))
print('')

termos = 10
total = 10
c = 1
decimo = t1 + (10 - 1) * r
total = total + termos

while c < 11:
    print('{} -> '.format(t1), end='')
    t1 += r
    c += 1
print('Fim')
