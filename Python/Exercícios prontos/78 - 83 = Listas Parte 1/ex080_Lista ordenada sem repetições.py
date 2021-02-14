lista = []
for c in range(0, 5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > lista[-1]:
        lista.append(n)
        print('Adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Adicionado na posição {pos} da lista...')
                break
            pos += 1
print('-=' * 30)
print(f'Os valores digitados em ordem foram {lista}')

#ou

list = []
for n in range(0, 5):
    p = int(input('Digite um valor: '))
    list.append(p)
    list.sort()
    if p == max(list):
        print('Adicionado ao final da lista...')
    else:
        print(f'Adicionado na posição {list.index(p)} da lista...')
print('-=' * 30)
print(f'Os valores digitados em ordem foram {list}')
