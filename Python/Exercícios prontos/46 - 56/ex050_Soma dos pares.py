par = 0
cont = 0
for c in range(1, 7):
    numb = int(input('Digite o {} número: '.format(c)))
    if numb % 2 == 0:
        par += numb
        cont += 1
print('Você informou {} números PARES e a soma foi {}'.format(cont, par))
