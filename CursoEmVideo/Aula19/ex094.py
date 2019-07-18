# 094 - Analisando dicionario

cont = 'S'
dic = {}
lista = []

soma = 0
media = 0

print('-' * 30)
print('{:^30}'.format('Analisando um'))
print('{:^30}'.format('DICIONÁRIO!'))
print('-' * 30)

while cont == 'S':
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).upper().strip()

    dic['nome'] = nome
    dic['idade'] = idade
    dic['sexo'] = sexo

    lista.append(dic.copy())

    print()
    cont = str(input('Deseja continuar [S/N]: ')).upper().strip()
    print('-' * 30)
    print()
print('-=' * 15)
print('{:^30}'.format('ANALISANDO'))
print()

print('- Pessoas cadastradas: {}'.format(len(lista)))

for pessoa in lista:
    soma += pessoa['idade']
media = soma / len(lista)
print('- Média de idade: {:.2f} anos.'.format(soma /len(lista)))

for pessoa in lista:
    if pessoa['sexo'] == 'F':
        print('- Mulheres cadastradas: {}'.format(pessoa['nome']))
print()

for pessoa in lista:
    if pessoa["idade"] > media:
        print('- Acima da média de idade: ')
        for k, v in pessoa.items():
            print('     {}: {}'.format(k, v))
