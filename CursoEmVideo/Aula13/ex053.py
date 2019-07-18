#palindromo
frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print('Inverso: {}'.format(inverso))
if junto == inverso:
    print('É um PALINDROMO')
else:
    print('NÃO é um Palindromo')