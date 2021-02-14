lista = []
auxiliar = []
maior = menor = 0
while True:
    auxiliar.append(str(input('Nome: ')))
    auxiliar.append(float(input('Peso: ')))
    if len(lista) == 0:
        maior = menor = auxiliar[1]
    else:
        if auxiliar[1] > maior:
            maior = auxiliar[1]
        if auxiliar[1] < menor:
            menor = auxiliar[1]
    lista.append(auxiliar[:])
    auxiliar.clear()
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
print('-=' * 30)
print(f'Ao todo, você cadastrou {len(lista)} pessoas.')
print(f'O maior peso foi de {maior}Kg. Peso de ', end='')
for p in lista:
    if p[1] == maior:
        print(f'[{p[0]}]', end='')
print()
print(f'O menor peso foi de {menor}Kg. Peso de ', end='')
for p in lista:
    if p[1] == menor:
        print(f'[{p[0]}]', end='')
print()

# ou(na minha solução encontrei uma falha no cadastro apenas de duas pessoas)

lista = []
auxiliar2 = []
maior = menor = 0
listmaior = []
listmenor = []
while True:
    auxiliar2.append(str(input('Nome: ')))
    auxiliar2.append(float(input('Peso: ')))
    if len(lista) == 0:
        maior = menor = auxiliar2[1]
    else:
        if auxiliar2[1] > maior:
            maior = auxiliar2[1]
            listmaior.clear()
            listmaior.append(auxiliar2[0])
        elif auxiliar2[1] == maior:
            listmaior.append(auxiliar2[0])
        if auxiliar2[1] < menor:
            menor = auxiliar2[1]
            listmenor.clear()
            listmenor.append(auxiliar2[0])
        elif auxiliar2[1] == menor:
            listmenor.append(auxiliar2[0])
    lista.append(auxiliar2[:])
    auxiliar2.clear()
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
print('-=' * 30)
print(f'Ao todo você cadastrou {len(lista)} pessoas.')
print(f'O maior peso foi de {maior:.1f}Kg. Peso de {listmaior}')
print(f'O menor peso foi de {menor:.1f}Kg. Peso de {listmenor}')
