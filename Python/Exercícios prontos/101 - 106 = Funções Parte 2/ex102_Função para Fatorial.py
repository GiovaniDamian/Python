def fatorial(numb, show=False):
    """
    -> Calcula o Fatorial de um número
    :param numb: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta
    :return: O valor do Fatorial de um número numb
    """
    f = 1
    while numb > 0:
        if show:
            print(f'{numb} ', end='')
            print(f'x ' if numb > 1 else ' = ', end='')
        f *= numb
        numb -= 1
    return f


print(fatorial(5, True))
