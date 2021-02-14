m = 0
velho = ''
idadevelho = 0
totam = 0
for p in range(1, 5):
    print('{} {}ª PESSOA {}'.format('-' * 5, p, '-' * 5))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()
    m += idade
    if idade > idadevelho and sexo in 'M':
        velho = nome
        idadevelho = idade
    elif sexo in 'F' and idade < 20:
        totam += 1
media = m / 4
print('A média de idade do grupo é de {:.2f}'.format(media))
print('O homem mais velho tem {} e se chama {}'.format(idadevelho, velho))
print('Ao todo são {} mulheres com menos de 20 anos'.format(totam))
