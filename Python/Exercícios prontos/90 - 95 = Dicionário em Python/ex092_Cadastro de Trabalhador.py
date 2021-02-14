from datetime import date
pessoa = dict()
pessoa['Nome'] = str(input('Nome: '))
Ano_nasc = int(input('Ano de Nascimento: '))
pessoa['Idade'] = date.today().year - Ano_nasc
pessoa['CTPS'] = int(input('Carteira de Trabalho (0 não tem): '))
if pessoa['CTPS'] != 0:
    pessoa['Contratação'] = int(input('Ano de Contratação: '))
    pessoa['Salario'] = int(input('Slário: R$'))
    pessoa['Aposentaria'] = (pessoa['Contratação'] - Ano_nasc) + 35
print('-=' * 20)
for v, k in pessoa.items():
    print(f' - {v} tem o valor {k}')

 # posso exportar from datetime import datetime e utilizo:
 # datetime.now().year