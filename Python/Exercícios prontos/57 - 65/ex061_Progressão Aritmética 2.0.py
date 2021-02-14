print('GERADOR DE PA')
print('-=' * 10)
termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
c = 1
print('{}'.format(termo), end=' - ')
while c < 10:
    n = termo + c * razao
    c += 1
    print(n, end=' - ')
print('FIM')

#ou

print('GERADOR DE PA')
print('-=' * 10)
termo = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
primeiro = termo
c = 1
while c <= 10:
    print('{} - '.format(primeiro), end='')
    primeiro += razao
    c += 1
print('FIM')
