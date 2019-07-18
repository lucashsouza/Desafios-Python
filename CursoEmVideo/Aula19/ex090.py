#090 - Média aluno

nome = str(input('Nome: '))
aluno = {'Nome': nome}

media = float(input(f'Média de {aluno["Nome"]}: '))

if media >= 6:
    aluno['Situacao'] = 'Aprovado'
else:
    aluno['Situacao'] = 'Reprovado'

aluno['Media'] = media

for k, v in aluno.items():
    print(f'{k} é igual a {v}')

print(aluno["Situacao"])
