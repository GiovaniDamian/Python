def aumentar(x=0, y=0):
    s = x + (x * y/100)
    return s


def diminuir(x=0, y=0):
    s = x - (x * y/100)
    return s


def dobro(x=0):
    s = 2 * x
    return s


def metade(x=0):
    s = x / 2
    return s


def formatacao(txt=0, moeda='R$'):
    return f'{moeda}{txt:.2f}'.replace('.', ',')
