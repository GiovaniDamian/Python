from math import floor
v = float(input('Digite um valor: '))
print('O valor digitado foi {} e a sua porção inteira é {}'.format(v, floor(v)))

#ou

from math import trunc
v = float(input('Digite um valor: '))
print('O valor digitado foi {} e a sua porção inteira é {}'.format(v, trunc(v)))
#Método Trunc retira somente a parte inteira do número

#ou

v = float(input('Digite um valor: '))
print('O valor digitado foi {} e a sua porção inteira é {}'.format(v, int(v)))
