from random import randint
from time import sleep


def sorteia(lista):
    print('Sorteando 5 valores da lista: ', end='')
    for cont in range(0, 5):
        n = randint(1, 10)
        lista.append(n)
        print(f'{n} ', end='')
        sleep(0.3)
    print('Pronto!')


def pares(lista):
    soma = 0
    for c in numeros:
        if c % 2 == 0:
            soma += c
    print(f'Somendo os valores pares de {numeros} temos {soma}')


numeros = list()
sorteia(numeros)
pares(numeros)

#ou


def sorteia(lista):
    cont = 0
    print('Sorteando 5 valores da lista: ', end='')
    while cont < 5:
        numeros.append(randint(1, 10))
        cont += 1
    for num in numeros:
        print(f'{num} ', end='')
        sleep(0.5)
    print('Pronto!')
