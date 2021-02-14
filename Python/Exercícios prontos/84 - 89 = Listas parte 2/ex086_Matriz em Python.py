matri = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matri[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matri[l][c]:^5}]', end='')
    print()

# ou

matriz = []
for n in range(0, 3):
    for c in range(0, 3):
        p = int(input(f'Digite um valor para [{n}, {c}]: '))
        matriz.append(p)
for h in range(0, 3):
    print(f'[ {matriz[h]:^3} ]', end='')
print()
for i in range(3, 6):
    print(f'[ {matriz[i]:^3} ]', end='')
print()
for j in range(6, 9):
    print(f'[ {matriz[j]:^3} ]', end='')
