geral = list()
pessoas = dict()
soma = media = 0
while True:
    pessoas.clear()
    pessoas['Nome'] = str(input('Nome: ')).strip()
    while True:
        pessoas['Sexo'] = str(input('Sexo: [M/F] ')).upper()
        if pessoas['Sexo'] in 'FM':
            break
        print('ERRO! Por favor, digite apenas M ou F')
    pessoas['Idade'] = int(input('Idade: '))
    soma += pessoas['Idade']
    geral.append(pessoas.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N')
    if resp == 'N':
        break
print('-=' * 30)
print(f'A) Ao todo temos {len(geral)} pessoas cadastradas.')
media = soma / len(geral)
print(f'B) A média de idade é de {media:.1f} anos')
print(f'C) As mulheres cadastradas foram ', end='')
for v in geral:
    if v['Sexo'] == 'F':
        print(f'{v["Nome"]} ', end='')
print(f'\nD) Lista das pessoas que estão acima da média:')
for v in geral:
    if v['Idade'] > media:
        print('     ', end='')
        for k, i in v.items():
            print(f'{k} = {i};', end=' ')
        print()
print('<< ENCERRADO >>')
