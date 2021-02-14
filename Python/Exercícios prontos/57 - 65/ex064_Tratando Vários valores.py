cont = soma = 0
n = int(input('Digite um número: [999 para encerrar] '))
while n != 999:
    cont += 1
    soma += n
    n = int(input('Digite um número: [999 para encerrar] '))
print('Você digitou {} números e a soma entre eles foi {}'.format(cont, soma))
