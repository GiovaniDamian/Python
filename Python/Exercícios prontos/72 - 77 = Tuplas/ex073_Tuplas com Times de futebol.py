classificacao = ('Santos', 'Flamengo', 'São Paulo', 'Palmeiras', 'Corinthians',
                 'Atlético- MG', 'Internacional', 'Bahia', 'Athletico-PR', 'Botafogo',
                 'Grêmio' 'Goiás', 'Ceará', 'Vasco', 'Fortaleza', 'Cruzeiro', 'Chapecoense',
                 'Fluminense', 'CS', 'Avaí')
print('-=' * 15)
print(f'Lista de times do Brasileirão: {classificacao}')
print('-=' * 15)
print(f'Os 5 primeiros são {classificacao[:5]}')
print('-=' * 15)
print(f'Os 4 últimos são {classificacao[-4:]}')
print('-=' * 15)
print(f'Times em ordem alfabética: {sorted(classificacao)}')
print('-=' * 15)
print(f'A chapecoense está na {classificacao.index("Chapecoense")+1}ª posição')
