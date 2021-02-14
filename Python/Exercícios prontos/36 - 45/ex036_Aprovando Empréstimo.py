casa = float(input('Valor da casa: R$: '))
salario = float(input('Slário do comprador: R$'))
finan = int(input('Quantos anos de financiamento? '))
prest = (casa/finan)/12
print('Para pagar uma casa de R${:.2f} em {:.0f} anos a prestação será de R${:.2f}'.format(casa, finan, prest))
if salario * 0.3 <= prest:
    print('Empréstimo NEGADO!')
else:
    print('Empréstimo pode ser CONCEDIDO!')
