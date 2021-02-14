def voto(numb):
    from datetime import date
    idade = date.today().year - numb
    if idade < 16:
        print(f'Com {idade} anos: VOTO NEGADO')
    elif 16 <= idade < 18 or idade > 65:
        print(f'Com {idade} anos: VOTO Opcional')
    else:
        print(f'Com {idade} anos: VOTO obrigatório')


nasc = int(input('Ano de nascimento: '))
voto(nasc)
