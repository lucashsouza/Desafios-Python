print('=' * 10, '10 TERMOS DE UMA PA', '=' * 10)
t1 = int(input('Primeiro termo: '))
r = int(input('Razão: '))
print('')

termos = 10
total = 0
termo = t1
c = 1

while termos != 0:
    total = total + termos
    while c <= total:
        print('{} -> '.format(t1), end='')
        t1 += r
        c += 1
    print('PAUSA')
    termos = int(input('Quantos termos você quer mostrar a mais? '))
print('')
print('PA finalizada. O total de termos mostrados foi {}'.format(total))
