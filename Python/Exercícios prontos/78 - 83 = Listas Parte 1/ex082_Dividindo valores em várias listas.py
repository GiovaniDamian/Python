lista = []
pares = []
impares = []
while True:
    lista.append(int(input('Digite um número: ')))
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
for v in lista:
    if v % 2 == 0:
        pares.append(v)
    else:
        impares.append(v)
print('-=' * 30)
print(f'A lista completa é {lista}')
print(f'A lista de pares é {pares}')
print(f'A lista de ímpares é {impares}')
