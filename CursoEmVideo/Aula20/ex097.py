# Exercicio 097 - Função para texto

'''
    Faça um programa que tenha uma função chamada escreva(), que receba um texto
    qualquer como parâmetro e mostre uma mensagem com o tamanho adaptável
'''

def mensagem(txt):
    tam = len(txt)
    print('~'*tam)
    print(txt)
    print('~'*tam, '\n')

mensagem('Hello, world!')
mensagem('Python é a a melhor linguagem de programação')
