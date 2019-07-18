palavras = ('Aprender', 'Programar', 'Linguagem', 'Python', 'Estudar',
            'Praticar', 'Evoluir', 'Futuro', 'Programador')
print('{:^40}'.format('VOGAIS'))

for p in palavras:
    print(f'\nNa palavra "{p.upper()}" temos as vogais: ', end='')
    for l in p:
        if l.lower() in 'aeiou':
            print(l.upper(), end=' ')
    print('')
print('')
