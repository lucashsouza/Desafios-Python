def aumentar(preco, taxa=0, formatado=False):
    """

    Função com o objetivo de calcular o aumento de
    determinada porcentagem parametrizada.

    :param preco: Valor a ser calculado
    :param taxa: Porcentagem a ser calculada
    :param formatado: Valor será apresentado com o formato(R$00,00) ou não?
    :return: Valor calculado, formatado ou não.

    """

    resposta = preco + (preco * taxa/100)
    return resposta if formatado is False else moeda(resposta)


def diminuir(preco=0, taxa=0, formatado=False):
    """
    Função com o objetivo de calcular o desconto de
    determinada porcentagem parametrizada.

    :param preco: Valor a ser calculado
    :param taxa: Porcentagem a ser calculada
    :param formatado: Valor será apresentado com o formato(R$00,00) ou não?
    :return: Valor calculado, formatado ou não.

    """

    resposta = preco - (preco * taxa/100)

    if formatado:
        return moeda(resposta)
    else:
        return resposta


def dobro(preco=0, formatado=False):
    """
    Função com o objetivo de calcular o dobro do
    valor parametrizado.

    :param preco: Valor a ser calculado
    :param formatado: Valor será apresentado com o formato(R$00,00) ou não?
    :return: Valor calculado, formatado ou não.

    """

    resposta = preco * 2
    if formatado:
        return moeda(resposta)
    else:
        return resposta


def metade(preco=0, formatado=False):
    """
    Função com o objetivo de calcular a metade do
    valor parametrizado.

    :param preco: Valor a ser calculado
    :param formatado:  Valor será apresentado com o formato(R$00,00) ou não?
    :return: Valor calculado, formatado ou não.

    """
    resposta = preco / 2

    if formatado:
        return moeda(resposta)
    else:
        return resposta


def moeda(preco=0, moeda='R$'):
    """

    :param preco: Valor a ser calculado
    :param moeda: Valor a ser acrescentado 'R$'
    :return: Valor calculado Formatado para duas casas decimais
    """

    return f"{moeda}{preco:.2f}".replace('.', ',')


def resumo(preco=0, taxa1=0, taxa2=0):
    """
    Função responsável por resumir todas as informações a serem
    exibidas na tela.

    :param preco: Valor a ser calculado.
    :param taxa1: Taxa a ser acrescentada.
    :param taxa2: Taxa a ser descontada.
    :return: prints com as informações organizadas na tela.

    """
    print()
    print('~' * 30)
    print("Resumo do valor".center(30))
    print('~' * 30)
    print(f"Preço analisado: {moeda(preco)}")
    print('~' * 30)
    print(f"Dobro: {dobro(preco, True).center(32)}")
    print(f"Metade: {metade(preco, True).center(30)}")
    print(f"{taxa1}% Acrescimo: {aumentar(preco, taxa1, True).center(15)}")
    print(f"{taxa2}% Desconto: {diminuir(preco, taxa2, True).center(17)}")
    print('-'*30)
