"""Crie um programa que tenha uma função fatorial() que receba dois parâmetros:

1. Indique o número a calcular

2. Show (Valor lógico) indicando se será mostrado na tela o processo de
    cálculo do fatorial - Opcional
"""


def titulo():
    print('-' * 45)
    print('{:^45}'.format('Função Fatorial '))
    print('-' * 45)
    return ''


def fim():
    from time import sleep
    sleep(3)
    return '\n*Fim de programa..*'


def fatorial(num=1, show=False):
    """
    -> Calcula a fatorial de um número.

    :param num: Número a ser calculado fatorial.
    :param show: (opcional) Mostrar ou não a conta.

    :return: valor da fatorial do número.

    *Desenvolvido por Lucas Souza, github.com/lucashsouza *.
    """

    fat = 1

    for cnt in range(num, 0, -1):
        if show:
            print(f'{cnt}', end='')

            if cnt > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        fat *= cnt

    return fat

# PROGRAMA PRINCIPAL


print(titulo())


n = int(input('Digite um número: '))


# Show = True / Mostra a conta
# Show = False / Não mostra a conta

print(fatorial(n, show=True))
print()

# Visualizar Docstring da funçao Fatorial ()
help(fatorial)

print(fim())
