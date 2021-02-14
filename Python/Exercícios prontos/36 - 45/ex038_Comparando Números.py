n1 = float(input('Primeiro número: '))
n2 = float(input('Segundo número: '))
if n1 == n2:
    print('Os dois valores são IGUAIS')
elif n1 > n2:
    print('O {}primeiro{} número é maior!'.format('\033[33m', '\033[m'))
else:
    print('O {}segundo{} número é maior'.format('\033[31m', '\033[m'))
