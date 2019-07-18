#progressao aritmetica
print('=' * 10, '10 TERMOS DE UMA PA', '=' * 10)
t1 = int(input('Primeiro termo: '))
r = int(input('Razão: '))
decimo = t1 + (10 - 1) * r
for n in range(t1, decimo + r, r):
    print('{} '.format(n), end='-> ')
print('FIM :)')
'''pa = n = t1 + (n - 1) * r
print(pa)'''
