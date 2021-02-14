opos = float(input('Comprimento do cateto oposto: '))
adj = float(input('Comprimento do cateto adjacente: '))
hip = (opos**2 + adj**2)**(1/2)
print('A hipotenusa vai medir {:.2f}'.format(hip))

#ou

import math
opos = float(input('Comprimento do cateto oposto: '))
adj = float(input('Comprimento do cateto adjacente: '))
hip = math.hypot(opos, adj)
print('A hipotenusa vai medir {:.2f}'.format(hip))

#ou

from math import hypot
opos = float(input('Comprimento do cateto oposto: '))
adj = float(input('Comprimento do cateto adjacente: '))
hip = hypot(opos, adj)
print('A hipotenusa vai medir {:.2f}'.format(hip))