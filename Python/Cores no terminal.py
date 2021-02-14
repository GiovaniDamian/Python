print('\033[31mOlá mundo')
print('\033[35;43mOlá mundo')
print('\033[7mOlá Mundo')
print('\033[7;30:mOlá Mundo')
print('\033[33;44mOlá mundo')
print('\033[7;33;44mOlá mundo')
print('\033[mOlá mundo')
a = 3
b = 4
print('Os valores são \033[32m{}\033[m e \033[31m{}\033[m!!'.format(a, b))

cores = {'limpa': '\033[m',
         'azul': '\033[34m',
         'amarelo': '\033[33m',
         'pretoebranco': '\033[7;30m'}
print('olá mundo {}OOOO{}!!!'.format(cores['azul'],cores['limpa']))

cores = ('\033[m',          # 0 - Sem cores
         '\033[0;30;41m',   # 1 - vermelho
         '\033[0;30;42m',   # 2 - verde
         '\033[0;30;43m',   # 3 - amarelo
         '\033[0;30;44m',   # 4 - azul
         '\033[0;30;45m',   # 5 - roxo
         '\033[7;30m'       # 6 - branco
         )
print(f' {cores[6]}Olá mundo{cores[0]}')