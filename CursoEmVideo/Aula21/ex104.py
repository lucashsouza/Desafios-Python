"""
Crie um programa que tenha função leiaInt(), que vai funcionar de forma semelhante
ao input() do Python, só que fazendo a validação para aceitar apenas
valores númericos.

Exemplo: n = leiaInt('Digite um número: ')

"""
# FUNÇÕES


def titulo():
    print('-' * 45)
    print('{:^45}'.format('Função para Ler apenas números inteiros. '))
    print('-' * 45)
    return ''


def fim():
    from time import sleep
    sleep(3)
    return '\n*Fim de programa..*'


def leiaint(mensagem):
    ok = False
    valor = 0

    while True:
        num = str(input(mensagem))

        if num.isnumeric():
            valor = int(num)
            ok = True

        else:
            print('\033[0;31mERRO! Digite um número INTEIRO válido.\033[m')

        if ok:
            break

    return valor


# PROGRAMA PRINCIPAL
print(titulo())

numero = leiaint('Digite um número: ')
print(f'Você acabou de digitar o número {numero}')

print(fim())
