name = str(input('Digite seu nome completo: ')).strip() #Utiliza o strip para eliminar possíveis espaços em branco
sep = name.split()
tot = ''.join(sep)
print('Analisando o seu nome...')
print('Seu nome em maiúscula é {}'.format(name.upper()))
print('Seu nome em minúscula é {}'.format(name.lower()))
print('Seu nome tem ao todo {} letras'.format(len(tot)))
print('Seu primeiro nomé é {} e ele tem {} letras'.format(sep[0], len(sep[0])))

#ou

name = str(input('Digite seu nome completo: ')).strip()
sep = name.split()
tot = ''.join(sep)
print('Analisando o seu nome...')
print('Seu nome em maiúscula é {}'.format(name.upper()))
print('Seu nome em minúscula é {}'.format(name.lower()))
print('Seu nome tem ao todo {} letras'.format(len(name)-name.count(' ')))
print('Seu primeiro nome tem {} letras'.format(name.find(' ')))