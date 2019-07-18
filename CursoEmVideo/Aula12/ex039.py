nasc = int(input('Ano de nascimento: '))
atual = int(input('Ano atual: '))
idade = atual - nasc
if (idade == 18):
    print('Corre para se alistar')
elif(idade > 18):
    print('Passou da hora, moio')
    atraso = idade - 18
    print('Você se atrasou em {} ano(s)'.format(atraso))
elif(idade < 18) :
    print('Boa sorte, tua hora chegará')
    suspense = 18 - idade
    print('Faltam {} ano(s)'.format(suspense))