from random import choise
n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo alunoo: '))
n3 = str(input('Terceiro nome: '))
n4 = str(input('Quarto aluno: '))
lista = (n1, n2, n3, n4)
escolhido = choise(lista)
print('O aluno sorteado foi {}'.format(escolhido))