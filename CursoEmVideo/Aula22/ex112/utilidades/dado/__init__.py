def leiaDinheiro(mensagem):
    valido = False

    while not valido:
        entrada = str(input(mensagem).replace(",", ".").strip())

        if entrada.isalpha():
            print(f'\033[1;31mERRO 01: "{entrada}" PREÇO INVÁLIDO!.\n\033[m')

        elif entrada == "":
            print(f'\033[1;31mERRO 02: PREÇO NÃO ENCONTRADO!.\n\033[m')

        else:
            valido = True
            return float(entrada)

