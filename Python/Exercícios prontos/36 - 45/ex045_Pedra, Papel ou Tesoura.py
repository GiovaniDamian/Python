from random import randint
from time import sleep
print('''Sua opção:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual é a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!')
computador = randint(0, 2)
print('-=' * 20)
if computador == 0:
    computador = 'Pedra'
elif computador == 1:
    computador = 'Papel'
elif computador == 2:
    computador = 'Tesoura'
if jogador == 0:
    jogador = 'Pedra'
elif jogador == 1:
    jogador = 'Papel'
elif jogador == 2:
    jogador = 'Tesoura'
print('Computador jogou {}'.format(computador))
print('Jogador jogou {}'.format(jogador))
print('-='*20)
if computador == 'Pedra' and jogador == 'Pedra':
    print('EMPATE, JOGUE NOVAMENTE')
elif computador == 'Pedra' and jogador == 'Papel':
    print('JOGADOR VENCE')
elif computador == 'Pedra' and jogador == 'Tesoura':
    print('COMPUTADOR VENCE')
elif computador == 'Papel' and jogador == 'Pedra':
    print('COMPUTADOR VENCE')
elif computador == 'Papel' and jogador == 'Papel':
    print('EMPATE, JOGUE NOVAMENTE')
elif computador == 'Papel' and jogador == 'Tesoura':
    print('JOGADOR VENCE')
elif computador == 'Tesoura' and jogador == 'Pedra':
    print('JOGADOR VENCE')
elif computador == 'Tesoura' and jogador == 'Papel':
    print('COMPUTADOR VENCE')
elif computador == 'Tesoura' and jogador == 'Tesoura':
    print('EMPATE, JOGUE NOVAMENTE')

#OU

from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Sua opção:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual é a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!')
print('-=' * 20)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('-=' * 20)
if computador == 0:
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCE')
    elif jogador == 2:
        print('COMPUTADOR VENCE')
    else:
        print('JOGADA INVÁLIDA')
elif computador == 1:
    if jogador == 0:
        print('COMPUTADOR VENCE')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCE')
    else:
        print('JOGADA INVÁLIDA')
elif computador == 2:
    if jogador == 0:
        print('JOGADOR VENCE')
    elif jogador == 1:
        print('COMPUTADOR VENCE')
    else:
        print('JOGADA INVÁLIDA')
