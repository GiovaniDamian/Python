print('\nGERADOR DE PA')
print('-=' * 10)
termo = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
primeiro = termo
c = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while c <= total:
        print('{} - '.format(primeiro), end='')
        primeiro += razao
        c += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('Progressão finalizada com {} termos'.format(total))

#ou

print('GERADOR DE PA')
print('-=' * 10)
termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
c = 1
cont = 0
n = 0
print('{}'.format(termo), end=' - ')
while c < 10:
    n = termo + c * razao
    c += 1
    print(n, end=' - ')
print('PAUSA')
ntermo = int(input('Quantos termos você quer mostrar a mais? '))
while ntermo != 0:
    novo = 1
    while novo <= ntermo:
        pr = n + razao
        n = pr
        novo += 1
        cont += 1
        print(pr, end=' - ')
    print('PAUSA')
    ntermo = int(input('Quantos termos você quer mostrar a mais? '))
if ntermo == 0:
    print('Progressão finalizada com {} termos mostrados'.format(c+cont))
