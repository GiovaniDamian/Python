lista = list()
maior = 0
menor = 0
for n in range(0, 5):
    lista.append(int(input(f'Digite um valor para a Posição {n}: ')))
    if n == 0:
        maior = menor = lista[n]
    else:
        if lista[n] > maior:
            maior = lista[n]
        if lista[n] < menor:
            menor = lista[n]
print('=-' * 30)
print(f'Você digitou os valores {lista}')
print(f'O maior valor digitado foi {maior} nas posições ', end='')
for i, v in enumerate(lista):
    if v == maior:
        print(f'{i}...', end='')
print(f'\nO menor valor digitado foi {menor} nas posições ', end='')
for i, v in enumerate(lista):
    if v == menor:
        print(f'{i}...', end='')
