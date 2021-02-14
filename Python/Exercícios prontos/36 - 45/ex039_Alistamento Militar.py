from datetime import date
nasc = int(input('Ano de nascimento: '))
atual = date.today().year
anos = atual - nasc
print('Quem nasceu em {} tem {} anos em {}'.format(nasc, anos, atual))
if anos < 18:
    rest = 18 - anos
    print('Ainda faltam {} anos para o alistamento'.format(rest))
    print('Seu alistamento será em {}'.format(atual + rest))
elif anos > 18:
    alistado = anos - 18
    print('Você já deveria ter se alistado há {} anos'.format(alistado))
    print('Seu alistamento foi em {}'.format(atual - alistado))
else:
    print('Você tem se alistar IMEDIATAMENTE')
