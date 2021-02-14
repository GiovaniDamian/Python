print('-' * 30)
print('{:^30}'.format('LOJA SUPER BARATÃO'))
print('-' * 30)
name = ' '
preço = tot = mil = 0
while True:
    nome = str(input('Nome do Produto: '))
    preco = float(input('Preço: R$'))
    tot += preco
    if preço == 0 or preco < preço:
        preço = preco
        name = nome
    if preco > 1000:
        mil += 1
    final = ' '
    while final not in'SN':
        final = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if final == 'N':
        break
print('{:-^30}'.format(' FIM DO PROGRAMA '))
print(f'O total da compra foi R${tot:.2f}')
print(f'Temos {mil} custando mais de R$1000.00')
print(f'O produto mais barato foi {name} que custa R${preço:.2f}')
