numb = (int(input('Digite um número: ')),
        int(input('Digite outro número: ')),
        int(input('Digite mais um número: ')),
        int(input('Digite último número: ')))
print(f'Você digitou os valores {numb}')
print(f'O valor 9 apareceu {numb.count(9)} vezes')
if 3 in numb:
    print(f'O valor 3 apareceu na {numb.index(3) + 1}ª posição')
else:
    print(f'O valor 3 não foi digitado')
print(f'Os valores pares digitados forma ', end='')
for n in numb:
    if n % 2 == 0:
        print(n, end=' ')
