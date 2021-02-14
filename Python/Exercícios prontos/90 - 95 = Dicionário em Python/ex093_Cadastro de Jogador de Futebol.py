dados = dict()
dados['Nome'] = str(input('Nome do Jogador: '))
parti = int(input(f'Quantas partidas o {dados["Nome"]} jogou? '))
gols = list()
for cont in range(0, parti):
    gols.append(int(input(f'Quantos Gols na partida {cont}? ')))
dados['Gols'] = gols[:]
dados['Total'] = sum(gols)
print('-=' * 30)
print(dados)
print('-=' * 30)
for k, v in dados.items():
    print(f' O campo {k} tem o valor {v}')
print('-=' * 30)
print(f'O jogador {dados["Nome"]} jogou {len(dados["Gols"])} partidas')
for k, v in enumerate(dados["Gols"]):
    print(f' => Na partida {k}, fez {v} gols')
print(f'Foi um total de {dados["Total"]} Gols')
