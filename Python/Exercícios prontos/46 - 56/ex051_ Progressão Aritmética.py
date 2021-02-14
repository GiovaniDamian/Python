termo = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
for c in range(0, 10):
    n = termo + (c) * razão
    print('{} -'.format(n), end=' ')
print('ACABOU')

#ou

primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
décimo = primeiro + (10 - 1) * razão
for c in range(primeiro,décimo + razão, razão):
    print('{} '.format(c), end='- ')
print('ACABOU')