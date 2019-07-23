
def leiaInt(mensagem):
    while True:
        n1 = str(input(mensagem))

        try:
            teste = int(n1)

        except KeyboardInterrupt:
            print('\033[0;31mUsuário preferiu não digitar esse número. \33[m')
            valor = 0

        except(ValueError):
            print("\033[0;31mERRO 03: Valor inválido. \n \33[m")
            continue

        except():
            print('\033[0;31mERRO 01: ')
            print('Informe um número INTEIRO válido.\n \33[m')
            continue

        else:
            valor = int(n1)
            break

    return valor


def leiaFloat(mensagem):
    while True:
        n2 = str(input(mensagem))

        try:
            teste = float(n2)

        except KeyboardInterrupt:
            print("Informação não encontrada")

        except(ValueError):
            print("\033[0;31mERRO 03: Valor inválido. \n \33[m")
            continue

        except():
            print('\033[0;31mERRO: Informe um número REAL válido. \33[m')

        else:
            valor = float(n2)
            break

    return valor


def resultados(n1, n2):
    print(titulo('Valores informados: '))
    print(f"Inteiro: {n1}\nReal: {n2}")
    return ""


def titulo(mensagem):
    print('\n\033[1;94m {:^45}\033[m\n'.format(mensagem))
    return ''
