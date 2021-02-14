from time import sleep
cores = ('\033[m',          # 0 - Sem cores
         '\033[0;30;41m',   # 1 - vermelho
         '\033[0;30;42m',   # 2 - verde
         '\033[0;30;43m',   # 3 - amarelo
         '\033[0;30;44m',   # 4 - azul
         '\033[0;30;45m',   # 5 - roxo
         '\033[7;30m'       # 6 - branco
         )


def ajuda(ms):
    titulo(f'Acessando o manual do comando \'{ms}\'', 4)
    print(cores[6], end='')
    help(ms)
    print(cores[0], end='')
    sleep(0.5)


def titulo(txts, cor=0):
    tam = len(txts) + 4
    print(cores[cor], end='')
    print('~' * tam)
    print(f' {txts}')
    print('~' * tam)
    print(cores[0], end='')
    sleep(0.5)


c = ''
while True:
    titulo('SISTEMA DE AJUDA PYHELP', 2)
    c = str(input('Função ou Biblioteca > '))
    if c.upper() == 'FIM':
        break
    else:
        ajuda(c)
titulo('ATÉ LOGO!', 1)


#OU


def formatacao(txt):
    print('\033[1;30;42m~' * (len(txt) + 4), f'\n  \'{txt}\'  ')
    print('~' * (len(txt) + 4))
    print('\033[m', end='')
    sleep(0.5)


def chama(txt):
    global n
    while True:
        formatacao('SISTEMA DE AJUDA PYHELP')
        n = str(input(f'{txt}'))
        if n.upper() == 'FIM':
            sleep(0.5)
            print('\033[1;30;41m~' * (len('ATÉ LOGO!') + 4), f'\n  ATÉ LOGO!  ')
            print('~' * (len('ATÉ LOGO') + 4))
            print('\033[m', end='')
            break
        mens = f' Acessando o manual do comando {n} '
        print('\033[1;30;44m~' * (len(mens) + 4), f'\n {mens}')
        print('~' * (len(mens) + 4))
        sleep(1)
        print('\033[7;30m', end='')
        help(n)
        print('\033[m', end='')
        sleep(1)
    return txt


chama('Função ou Biblioteca > ')
