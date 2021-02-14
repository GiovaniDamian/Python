pessoas = dict()
pessoas['Nome'] = str(input('Nome: '))
pessoas['Media'] = float(input(f'Média de {pessoas["Nome"]}: '))
if pessoas['Media'] >= 7:
    pessoas['situacao'] = 'Aprovado'
elif 5 <= pessoas['Media'] < 7:
    pessoas['situacao'] = 'Recuperação'
else:
    pessoas['situacao'] = 'Reprovado'
for k, v in pessoas.items():
    print(f'{k} é igual a {v}')
