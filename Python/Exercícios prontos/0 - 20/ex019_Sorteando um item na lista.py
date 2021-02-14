import random
first = input('Primeiro Aluno: ')
second = input('Segundo Aluno: ')
third = input('Terceiro Aluno: ')
list = [first, second, third]
chosen = random.choice(list)
print(chosen)
