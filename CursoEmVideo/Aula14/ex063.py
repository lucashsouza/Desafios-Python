c = 3
t1 = 0
t2 = 1

print('=' * 22, '\nSEQUENCIA DE FIBONACCI')
print('=' * 22)
print(' ')
print('~' * 32)
n = int(input('Quantos termos você quer mostrar? '))
print('~' * 32)
print('{} -> {}'.format(t1, t2), end='')

while c <= n:
    t3 = t1 + t2
    print(' -> {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    c += 1
print('')
print('Fim')
