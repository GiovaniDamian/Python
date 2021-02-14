matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somac = pares = maiorl = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            pares += matriz[l][c]
    print()
print('-=' * 30)
print(f'A soma dos valores pares é {pares}')
for l in range(0, 3):
    somac += matriz[l][2]
print(f'A soma dos valores da terceira coluna é {somac}')
for c in range(0, 3):
    if c == 0:
        maiorl = matriz[1][c]
    elif matriz[1][c] > maiorl:
        maiorl = matriz[1][c]
print(f'O maior valor da segunda linha é {maiorl}')

# ou

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somac = pares = maiorl = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
        if c == 2:
            somac += matriz[l][c]
        if l == 1 and matriz[l][c] >= maiorl:
            maiorl = matriz[l][c]
        if matriz[l][c] % 2 == 0:
            pares += matriz[l][c]
print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
print('-=' * 30)
print(f'A soma dos valores pares é {pares}')
print(f'A soma dos valores da terceira coluna é {somac}')
print(f'O maior valor da segunda linha é {maiorl}')
