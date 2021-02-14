cont = tot = maior = menor = 0
prosseguir = 'S'
while prosseguir in 'S':
    numb = int(input('Digite um número: '))
    cont += 1
    tot += numb
    if cont == 1:
        maior = menor = numb
    else:
        if numb < menor:
            menor = numb
        elif numb > maior:
            maior = numb
    prosseguir = str(input('Quer continuar? [S/N]')).strip()[0].upper()
media = tot / cont
print('Você digitou {} números e amédia foi {}'.format(cont, media))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))
