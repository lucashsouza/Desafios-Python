resp = str(input('Informe seu sexo [M/F]: ')).strip().upper()[0]
while resp not in 'MmFf':
    resp = str(input('Dados inválidos! Informe seu sexo: ')).strip().upper()[0]

print('Sexo {} registrado com sucesso'.format(resp))