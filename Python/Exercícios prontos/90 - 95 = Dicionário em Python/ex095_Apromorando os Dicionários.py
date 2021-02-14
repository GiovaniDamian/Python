time = list()
dados = dict()
while True:
    dados.clear()
    dados['Nome'] = str(input('Nome do Jogador: '))
    parti = int(input(f'Quantas partidas o {dados["Nome"]} jogou? '))
    gols = list()
    for cont in range(0, parti):
        gols.append(int(input(f'Quantos Gols na partida {cont}? ')))
    dados['Gols'] = gols[:]
    dados['Total'] = sum(gols)
    time.append(dados.copy())
    while True:
        cont = str(input('Quer continuar? [S/N] ')).upper()[0]
        if cont in 'SN':
            break
        print('ERRO! Responda apenas S ou N. ')
    if cont == 'N':
        break
print('-=' * 30)
print('COD ', end='')
for i in dados.keys():
    print(f'{i:<15}', end='')
print()
print('-' * 50)
for k, v in enumerate(time):
    print(f'{k:>4} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
while True:
    resp = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if resp == 999:
        break
    if resp >= len(time):
        print(f'ERRO! Não existe jogador com o código {resp}')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[resp]["Nome"]}: ')
        for i, g in enumerate(time[resp]["Gols"]):
            print(f'    No jogo {i+1} fez {g} gols.')
        print('-' * 50)
print('<< VOLTE SEMPRE >>')