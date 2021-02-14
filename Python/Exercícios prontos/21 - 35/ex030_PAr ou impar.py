jogador = int(input('Me diga um número qualquer: '))
par = jogador % 2
if par == 0:
    print('O número {} é PAR'.format(jogador))
else:
    print('O número {} é IMPAR'.format(jogador))
