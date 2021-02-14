import moeda

p = float(input('Digite o preço: R$'))
print(f'A metade de {moeda.formatacao(p)} é {moeda.formatacao(moeda.metade(p))}')
print(f'O dobro de {moeda.formatacao(p)} é {moeda.formatacao(moeda.dobro(p))}')
print(f'Aumentando 10%, temos {moeda.formatacao(moeda.aumentar(p, 10))}')
