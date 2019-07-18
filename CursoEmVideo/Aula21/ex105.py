"""
Faça um programa que tenha uma função notas() que pode receber várias notas de alunos
e vai retornar um dicionário com as seguintes informações:

    1. Quantidade de notas.
    2. A maior nota
    3. Menor nota
    4. Média da turma
    5. A situação (Opicional)

Adicione também as docstrings das função

"""


# Funções

def notas(*n, sit=False):
    """

notas(*n, sit=False)

    -> Função para analisar notas e situações de vários alunos.

    :param n: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação

    :return: dicionário com várias informações sobre a situação da turma.
    """

    r = dict()

    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n) / len(n)

    if sit:
        if r['media'] >= 7:
            r['situacao'] = 'BOA'

        elif r['media'] >= 5:
            r['situacao'] = 'RAZOAVEL'

        else:
            r['situacao'] = 'RUIM'

    return r


# Programa Principal

# help(notas)


resposta = notas(5.5, 2.5, 1.5, sit=True)

print(resposta)
