import math
angulo = float(input('Digite o ângulo que você deseja: '))
seno = math.sin(math.radians(angulo))
cos = math.cos(math.radians(angulo))
tang = math.tan(math.radians(angulo))
print('O ângulo de {:.0f} tem o SENO de {:.2f}\nO ângulo de {:.0f} tem o COSSENO de {:.2f}\nO ângulo de {:.0f} tem a TANGENTE de {:.2f}'.format(angulo, seno, angulo, cos, angulo, tang))

#ou

from math import sin, cos, radians, tan
angulo = float(input('Digite o ângulo que você deseja: '))
seno = sin(radians(angulo))
cos = cos(radians(angulo))
tang = tan(radians(angulo))
print('O ângulo de {} tem o SENO de {:.2f}\nO ângulo de {} tem o COSSENO de {:.2f}\nO ângulo de {} tem a TANGENTE de {:.2f}'.format(angulo, seno, angulo, cos, angulo, tang))
