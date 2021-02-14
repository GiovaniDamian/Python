distancia = float(input('Qual a distância de sua viagem? '))
print('Você está preste a começar uma viagem de {:.1f} KM'.format(distancia))
if distancia > 200:
    t = distancia * 0.45
else:
    t = distancia * 0.5
print('E o preço da sua passagem será de R${:.2f}'.format(t))

#OU

distancia = float(input('Qual a distância de sua viagem? '))
print('Você está preste a começar uma viagem de {:.1f} KM'.format(distancia))
t = distancia * 0.45 if distancia > 200 else distancia * 0.5
print('E o preço da sua passagem será de R${:.2f}'.format(t))