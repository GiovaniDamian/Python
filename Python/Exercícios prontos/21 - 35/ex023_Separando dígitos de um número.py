numb = int(input('Informe um número: '))
u = numb // 1 % 10
d = numb // 10 % 10
c = numb // 100 % 10
m = numb // 1000 % 10
print('Analisando o número {}'.format(numb))
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))
