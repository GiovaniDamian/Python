from random import randint
print('=-' * 20)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-' * 20)
v = 0
while True:
    computador = randint(0, 10)
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
        jogador = int(input('Digite um valor: '))
        total = jogador + computador
        print('-' * 30)
        print(f'Você jogou {jogador} e o computador {computador}. Total de {total}', end=' ')
        print('DEU PAR' if total % 2 == 0 else 'DEU ÍMPAR')
        print('-' * 30)
    if tipo == 'P':
        if total % 2 ==0:
            print('Você VENCEU!!')
            v += 1
        else:
            print('Você PERDEU!!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você VENCEU!!')
            v += 1
        else:
            print('Você PERDEU!!')
            break
    print('Vamos jogar novamente...')
print('=-' * 20)
print(f'GAME OVER! Você venceu {v} vezes.')

#ou

from random import randint
print('=-' * 20)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-' * 20)
cont = 0
while True:
    pi = str(input('Par ou Ímpar? [P/I] ')).strip().upper()
    v = int(input('Digite um valor: '))
    comp = randint(0, 10)
    tot = v + comp
    rpi = tot % 2
    if rpi == 0:
        print('-' * 30)
        print(f'Você jogou {v} e o computador {comp}. Total de {tot} DEU PAR ')
        print('-' * 30)
        if rpi == 0 and pi == 'P' or rpi != 0 and pi == 'I':
            cont += 1
            print('Você VENCEU!')
            print('Vamos jogar novamente...')
        elif rpi == 0 and pi == 'I' or rpi != 0 and pi == 'P':
            print('Você PERDEU!')
            break
    elif rpi != 0:
        print('-' * 30)
        print(f'Você jogou {v} e o computador {comp}. Total de {tot} DEU ÍMPAR ')
        print('-' * 30)
        if rpi == 0 and pi == 'P' or rpi != 0 and pi == 'I':
            cont += 1
            print('Você VENCEU!')
            print('Vamos jogar novamente...')
        elif rpi == 0 and pi == 'I' or rpi != 0 and pi == 'P':
            print('Você PERDEU!')
            break
print(f'GAME OVER! Você venceu {cont} vezes.')
