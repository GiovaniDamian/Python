exp = str(input('Digite a expressão: '))
lista = []
for letra in exp:
    if letra == '(':
        lista.append('(')
    elif letra == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(')')
            break
if len(lista) == 0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está errada!')

#ou

exp = str(input('Digite a expressão: ')).strip()
print(exp.index('('))
lista = []
lista2 = []
for letra in exp:
    if letra == '(':
        lista += '('
    if letra == ')':
        lista2 += ')'
if len(lista) == len(lista2):
    print('Expressão válida')
else:
    print('Expressão inválida')
