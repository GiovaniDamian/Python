from time import sleep


def analisador(* num):
    print('-=' * 30)
    print('Analisando os valores passados...')
    sleep(1)
    maior = 0
    for c in num:
        print(f'{c} ', end='')
        sleep(0.5)
        if c >= maior:
            maior = c
    print(f'Foram informados {len(num)} valores ao todo')
    print(f'O maior valor informado foi {maior}')


analisador(2, 9, 4, 5, 7, 1)
analisador(4, 7, 0)
analisador(1, 2)
analisador(6)
analisador()
