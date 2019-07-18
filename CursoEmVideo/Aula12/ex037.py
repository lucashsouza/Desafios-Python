n = int(input('Digite um número: '))
print('Escolha a base de conversão: ')
print('[1] para BINÁRIO\n[2] para OCTAL\n[3] para HEXADECIMAL')
esc = int(input('Sua opção: '))
if (esc == 1):
    print('')
    print('O valor {} em binário é: {}'.format(n, bin(n)[2:]))
elif (esc == 2):
    print('')
    print('O valor {} em octal é: {}'.format(n, oct(n)[2:]))
elif (esc == 3):
    print('')
    print('O valor {} em hexadecimal é: {}'.format(n, hex(n)[2:]))
else:
    print('Opção inválida!')