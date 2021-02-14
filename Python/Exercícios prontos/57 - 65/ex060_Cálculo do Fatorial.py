from math import factorial
numb = int(input('Digite um número para calcular seu fatorial: '))
f = factorial(numb)
print('O fatorial de {} é {}'.format(numb, f))

#ou

numb = int(input('Digite um número para calcular seu fatorial: '))
c = numb
f = 1
print('Calculando {}! = '.format(numb), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f))
