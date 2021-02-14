peso = float(input('Qual o seu peso? (Kg) '))
altura = float(input('Qual a sua altura? (m) '))
imc = peso / (altura ** 2)
print('O IMC dessa pessoa é de {:.1f}'.format(imc))
if imc < 18.5:
    print('Você está ABAIXO DO PESO!')
elif imc < 25:
    print('PARABÉNS, você está na faixa de PESO NORMAL')
elif imc < 30:
    print('Você está em SOBREPESO')
elif imc < 40:
    print('Você está em OBESIDADE')
else:
    print('Você está com OBESIDADE MÓRBIDA')
