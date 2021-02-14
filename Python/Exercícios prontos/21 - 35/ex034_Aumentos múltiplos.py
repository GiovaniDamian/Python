salario = float(input('Qual é o salário do funcionário? R$ '))
if salario > 1250:
    novo = salario * 1.1
else:
    novo = salario * 1.15
print('Quem ganahava R${:.2f} passa a ganhar R${:.2f} agora'.format(salario, novo))
