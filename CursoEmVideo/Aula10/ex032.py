ano = int(input('Digite um ano: '))
if (ano % 4 == 0) or (ano % 400 == 0):
    print('O ano de {} é bissexto'.format(ano))
else:
    print('O ano de {} não é bissexto'.format(ano))