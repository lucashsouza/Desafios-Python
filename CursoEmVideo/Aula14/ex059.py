opcao = 0
r = int()
while opcao != 5:
    n1 = int(input('Primeiro valor: '))
    n2 = int(input('Segundo valor: '))
    print('')
    print('''[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos numeros
[5] Sair do programa ''')
    print('')
    opcao = int(input('Opção: '))
    print('')

    if opcao == 1:
        r = n1 + n2
        print('A soma entre {} e {} é igual a {}'.format(n1, n2, r))
        print('')

    elif opcao == 2:
        r = n1 * n2
        print('A multiplicação entre {} e {} é igual a {}'.format(n1, n2, r))
        print('')

    elif opcao == 3:
        if n1 > n2:
            r = n1
        elif n2 > n1:
            r = n2
        print('O maior valor entre {} e {} é {}'.format(n1, n2, r))
        print('')

    elif opcao == 4:
        print('Informe os números novamente! ')
        print('')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo número: '))
        print('''
[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos numeros
[5] Sair do programa ''')
        print('')
        opcao = int(input('Sua opção: '))

        if opcao == 1:
            r = n1 + n2
            print('A soma entre {} e {} é igual a {}'.format(n1, n2, r))
            print('')

        elif opcao == 2:
            r = n1 * n2
            print('A multiplicação entre {} e {} é igual a {}'.format(n1, n2, r))
            print('')

        elif opcao == 3:
            if n1 > n2:
                r = n1
            elif n2 > n1:
                r = n2
            print('O maior valor entre {} e {} é {}'.format(n1, n2, r))
            print('')

        elif opcao == 5:
            print('Finalizando..')

    elif opcao == 5:
        print('Finalizando..')
    else:
        print('Opção inválida! ')
