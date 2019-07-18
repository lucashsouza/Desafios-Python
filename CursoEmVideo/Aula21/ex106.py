"""
Faça um mini Sistema que utilize o interactive help do Python.
O usuário vai digitar o comando e o manual vai aparecer.
Quando o usuário digitar FIM, o programa se encerrará.


"""

# Funções


def ajuda(com):
    help(com)


def titulo(mensagem):
    tamanho = len(mensagem) + 4
    print('~' * tamanho)
    print(f' {mensagem} ')
    print('~' * tamanho)


# Programa Principal


titulo('SISTEMA DE AJUDA PYHELP')

comando = ''

while True:
    comando = str(input('\n Função ou Biblioteca > '))

    if comando.upper() == 'FIM':
        print()
        titulo('ATÉ LOGO')
        break

    else:
        ajuda(comando)
