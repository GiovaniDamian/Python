from random import randint
computador = randint(0, 10)
print('''Sou seu computador....
    Acabei de pensar em um número entre 0 e 10. 
      Será que você consegue adivinhar qual foi?''')
jogador = int(input('Qual é o seu palpite? '))
cont = 1
while jogador != computador:
    cont += 1
    if jogador < computador:
        print('Mais...Tente mais uma vez.')
    elif jogador > computador:
        print('Menos...Tente mais uma vez.')
    jogador = int(input('Qual é o seu palpite? '))
print('PARABÉNS! Acertou com {} tentativas.'.format(cont))

#ou

from random import randint
computador = randint(0, 10)
print('''Sou seu computador....
    Acabei de pensar em um número entre 0 e 10. 
      Será que você consegue adivinhar qual foi?''')
acertou = False
palpite = 0
while not acertou:
    jogador = int(input('Qual é seu palpite? '))
    palpite += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais...Tente mais uma vez.')
        elif jogador > computador:
            print('Menos...Tente mais uma vez.')
print('Acertou com {} tentativas. PARABÉNS!'.format(palpite))