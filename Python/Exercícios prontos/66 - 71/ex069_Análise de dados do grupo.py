homens = idade18 = idade20 = 0
print('-' * 25)
while True:
    print('{:^25}'.format('CADASTRE UMA PESSOA'))
    print('-' * 25)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F]')).strip().upper()[0]
        print('-' * 25)
    if idade > 18:
        idade18 += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        idade20 += 1
    cont = ' '
    while cont not in 'SN':
        cont = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        print('-' * 25)
    if cont == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {idade18}')
print(f'Ao todo temos {homens} homens cadastrados')
print(f'E temos {idade20} mulheres com menos de 20 anos')

idade18 = homens = idade20 = 0
cont = ' '
print('-' * 25)
while cont != 'N':
    print('{:^25}'.format('CADASTRE UMA PESSOA'))
    print('-' * 25)
    idade = int(input('Idade: '))
    if idade > 18:
        idade18 += 1
    sexo = str(input('Sexo: [M/F} ')).strip().upper()
    if sexo == 'F' and idade < 20:
        idade20 += 1
    elif sexo == 'M':
        homens += 1
    print('-' * 25)
    cont = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    print('-' * 25)
print(f'Total de pessoas com mais de 18 anos: {idade18}')
print(f'Ao todo temos {homens} homens cadastrados')
print(f'E temos {idade20} mulheres com menos de 20 anos')
