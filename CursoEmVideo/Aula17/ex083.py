print('=' * 30)
print('{:^30}'.format('Expressão'))
print('=' * 30)
print('')

e = str(input("Digite sua expressão: ")).strip()
p1 = e.count("(")
p2 = e.count(")")

if p1 == p2:
    print("Sua expressão está correta !")

else:
    print("Sua expressão está incorreta !")
