#ex 089 - Boletim

#obs: alunos a partir de 0 na lista

aluno = list([[], [], [], []]) #nova lisa
resp = 'S' #validar loop

while True:
    alunos = []

    if resp == 'S':
        n = str(input('Nome: '))
        nota1 = float(input('Nota 1: '))
        nota2 = float(input('Nota 2: '))
        #processamento de entradas

        media = (nota1 + nota2) / 2
        aluno[0].append(n)
        aluno[1].append([nota1, nota2])
        aluno[2].append(media)

        print()
        resp = str(input('Continuar [S/N]: ')).strip().upper()
        print()

    #finalizar o programa

    if resp == 'N':
        break

while True: #mostrando boletim
    ind = int(input('Qual aluno [999 finaliza]: '))

    if ind == 999:
        print('Finalizando...')
        break

    print('-' * 20)
    print('{:^20}'.format('Boletim'))
    print('-' * 20)
    print(f'{aluno[0][ind]}')
    print()
    print(f'Notas: {aluno[1][ind]}')

    #processamento da média:

    print()
    if media <= 5.0:
        print(f'Média: {media}')
        print()
        print('R E P R O V A D O')
    elif media <= 6.5:
        print(f'Média: {media}')
        print()
        print('Abaixo da média')
    elif media <= 8.0:
        print(f'Média: {media}')
        print()
        print('B O M')
    elif media <= 9.0:
        print(f'Média: {media}')
        print()
        print('M U I T O  B O M!')
    elif media <= 10:
        print(f'Média: {media}')
        print()
        print('P A R A B E N S!')
    print()
    print('-' * 20)
