lista = []
resp = ''
while resp != 'N':
    n = int(input('Digite um valor: '))
    if n not in lista:
        lista.append(n)
        print('Valor adicionado com sucesso..')
    else:
        print('Valor duplicado! Não vou adicionar...')
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
print('-=' * 40)
lista.sort()
print(f'Você digitou os valores {lista}')
