jogador = float(input('Qual a velocidade atual do carro? '))
if jogador > 80:
    m = (jogador - 80) * 7
    print('MULTADO! Você exceu o limite permitido que é de 80Km/h\nVocê deve pagar uma multa de R${:.2f}'.format(m))
print('Tenha um bom dia! Diriga com segurança!')
