n1 = float(input('Nota 1: '))
n2 = float(input('Nota 2: '))
m = (n1 + n2) / 2

print('Tirando {:.1f} e {:.1f}, a média do aluno é {}'.format(n1, n2, m))

if 7 > m >= 5:
    print('O aluno está em RECUPERAÇÃO!')
elif m < 5:
    print('O aluno está REPROVADO!')
elif m >= 7:
    print('O aluno está APROVADO!!')
