from random import randint
n1, n2, n3, n4, n5 = randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9)
tup = n1, n2, n3, n4, n5
print(f'Os valores sorteados foram {tup}')
print(f'O maior número é {max(tup)}')
print(f'O menor número é {min(tup)}')
