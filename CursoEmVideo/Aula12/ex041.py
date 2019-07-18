nasc = int(input('Ano de nascimento: '))
idade = 2018 - nasc

if idade <= 9:
    print('Categoria: Mirim')
elif idade <= 14:
    print('Categoria: Infantil')
elif idade <= 19:
    print('Categoria: Júnior')
elif idade <= 20:
    print('Categoria: Sênior')
elif idade >= 21:
    print('Categoria: Master')