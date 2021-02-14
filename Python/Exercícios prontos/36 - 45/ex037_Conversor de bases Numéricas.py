numb = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão: 
 [ 1 ] Converter para BINÁRIO
 [ 2 ] Converter para OCTAL
 [ 3 ] Converter para HEXADECIMAL''')
print(('-/-') * 15)
escolha = int(input('Sua opção: '))
if escolha == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(numb, bin(numb)[2:]))
elif escolha == 2:
    print('{} Convertido para OCTAL é igual a {}'.format(numb, oct(numb)[2:]))
elif escolha == 3:
    print('{} Convertido para HEXADECIMAL é igual a {}'.format(numb, hex(numb)[2:]))
else:
    print('Opção inválida. Tente novamente')


