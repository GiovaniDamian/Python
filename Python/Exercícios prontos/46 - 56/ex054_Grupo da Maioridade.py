from datetime import date
atual = date.today().year - 18 #aqui pode ser acrescentado uma linha identificando a idade para diminuir da data atual
maior = 0
menor = 0
for c in range(1, 8):
    nasc = int(input('Em que ano a {}ª pessoa nasceu? '.format(c)))
    if nasc < atual:
        menor += 1
    else:
        maior += 1
print('Ao todo tivemos {} pessoas maiores de idade'.format(maior))
print('E também tivemos {} pessoas menores de idade'.format(menor))
