n = 0
qnt = 0
s = 0

print('Digite numeros e veja sua soma')
print('999 finaliza o programa')
print('')

while n != 999:
    n = int(input(f'{qnt + 1}° Número: '))
    qnt += 1
    if n == 999:
        break
    s += n
print('')
print(f'Foram digitados {qnt} números, e a soma entre eles é {s}')
