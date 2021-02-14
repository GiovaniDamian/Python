from random import shuffle
first = input('Primeiro Aluno: ')
second = input('Segundo Aluno: ')
third = input('Terceiro Aluno: ')
list = [first, second, third]
shuffle(list)
print('A ordem de apresentação será\n {}'.format(list))