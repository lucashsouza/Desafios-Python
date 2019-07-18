v = []
for n in range(0, 5):
    v.append(int(input(f'{n +1}° Valor: ')))
lista = list(v)
print(f'Você digitou {lista}\n'
      f'O maior número da lista é {max(lista)}\n'
      f'O menor número da lista é {min(lista)}\n')
