ficha = list()
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    ficha.append([nome, nota1, nota2])
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
print('-=' * 30)
print(f'{"No.":<4} {"NOME":<10} {"MÉDIA":8}')
print('-' * 30)
for n in range(0, len(ficha)):
    print(f'{n:<4} {ficha[n][0]:<10} {(ficha[n][1] + ficha[n][2]) / 2:>8.1f}')
# ou
# for i, a in enumerate(ficha):
#   print(f'{i:<4}{a[0]:<10}{(a[1]/a[2]):>8.1f}')
while True:
    print('-' * 30)
    n = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if n == 999:
        print('FINALIZANDO...')
        break
    if n <= len(ficha) - 1:
        print(f'Notas de {ficha[n][0]} são [{ficha[n][1]}, {ficha[n][2]}]')
print('<<< VOLTE SEMPRE >>>')
