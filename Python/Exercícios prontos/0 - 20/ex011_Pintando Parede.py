largura = float(input('Largura da parede: '))
altura = float(input('Altura da parede: '))
area = largura*altura
print('Sua parede tem a dimensão de {}x{} e sua áre é de {}m²'.format(largura, altura, area))
print('Para pintar essa parede, você precisará de {}L de tinta'.format(area/2))