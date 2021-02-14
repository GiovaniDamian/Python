def area(a, b):
    m = a * b
    print(f'A áre de um terreno {a} x {b} é de  {m} m²')


print('CONTROLE de TERRENOS')
print('-' * 20)
area((float(input('LAGURA (m): '))), (float(input('COMPRIMENTO (m): '))))

#ou
print('CONTROLE de TERRENOS')
print('-' * 20)
l = float(input('Largura (m): '))
c = float(input('Comprimento (m): '))
area(l, c)