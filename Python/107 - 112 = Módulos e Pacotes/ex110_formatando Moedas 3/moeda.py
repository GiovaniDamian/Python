def aumentar(x=0, y=0, z=True):
    s = x + (x * y/100)
    return s if z is False else formatacao(int(s))


def diminuir(x=0, y=0, z=True):
    s = x - (x * y/100)
    return s if z is False else formatacao(int(s))


def dobro(x=0, y=True):
    s = 2 * x
    return s if y is False else formatacao(int(s))


def metade(x=0, y=True):
    s = x / 2
    return s if y is False else formatacao(int(s))


def formatacao(txt=0, moeda='R$'):
    return f'{moeda}{txt:.2f}'.replace('.', ',')


def resumo(x=0, y=0, z=0):
    print('-' * 30)
    print(f'{"RESUMO DO VALOR":^30}')
    print('-' * 30)
    print(f'Preço analisado: \t{formatacao(x)}')
    print(f'Dobro do preço:  \t{dobro(x)}')
    print(f'Metade do preço: \t{metade(x)}')
    print(f'{y}% de aumento: \t{aumentar(x, y)}')
    print(f'{z}% de redução: \t{diminuir(x, z)}')
    print('-' * 30)
