import moeda

p = float(input('Digite o preço: R$'))
print(f'A metade de {moeda.formatacao(p)} é {moeda.metade(p)}')
print(f'O dobro de {moeda.formatacao(p)} é {moeda.dobro(p)}')
print(f'Aumentando 10%, temos {moeda.aumentar(p, 10)}')
