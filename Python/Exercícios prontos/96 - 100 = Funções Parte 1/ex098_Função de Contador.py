from time import sleep


def contagem(a, b, c):
    if c < 0:
        c *= -1
    if c == 0:
        c = 1
    print('-=' * 20)
    print(f'Contagem de {a} até {b} de {c} em {c}')
    sleep(1)
    for p in range(a, b + 1, c):
        print(f'{p} ', end='')
        sleep(0.5)
    if a > b:
        for p in range(a, b - 1, - c):
            print(f'{p} ', end='')
            sleep(0.5)
    print('FIM')


contagem(1, 10, 1)
contagem(10, 0, 2)
print('-=' * 20)
print('Agora é a sua vez de personalizar a contagem!')
contagem(int(input('Início: ')), int(input('Fim: ')), int(input('Passo: ')))

#ou


def contagem(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print('-=' * 20)
    print(f'Contagem de {i} até {f} de {p} em {p}')
    sleep(1)
    if i <= f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='')
            sleep(0.5)
            cont += p
        print('FIM!')
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='')
            sleep(0.5)
            cont -= p
        print('FIM!')


contagem(1, 10, 1)
contagem(10, 0, 2)
print('Agora é a sua vez de personalizar a contagem!')
contagem(int(input('Início: ')), int(input('Fim: ')), int(input('Passo: ')))
