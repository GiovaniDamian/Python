numb = int(input('Digite um número: '))
cont = 0
for c in range(1, numb + 1):
    formato = '\033[m'
    if numb % c == 0:
        cont += 1
        formato = '\033[34m'
    print('{} {} {}'.format(formato, c, '\033[m'), end='')
print('\nO número {} foi divisível {} vezes'.format(numb, cont))
if cont == 2:
    print('E por isso ele É PRIMO')
else:
    print('E por isso ele NÃO É PRIMO')
