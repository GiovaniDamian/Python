print('{:=^40}'.format('LOJAS TFD'))
compra = float(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opcao = int(input('Qual é a opção? '))
if opcao == 1:
    total = compra * 0.9
elif opcao == 2:
    total = compra * 0.95
elif opcao == 3:
    total = compra
    parcela = compra / 2
    print('Sua compra será parcelada em 2x de R${:.2f} SEM JUROS'.format(parcela))
elif opcao == 4:
    nparcela = int(input('Quantas parcelas? '))
    total = compra * 1.2
    parcela = total / nparcela
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS'.format(nparcela, parcela))
else:
    total = compra
    print('OPÇÃO INVÁLIDA de pagamento. Tente novamente')
print('Sua compra de R${:.2f} vai custar R${:.2f} no final'.format(compra, total))
