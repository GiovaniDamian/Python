print('=' * 30)
print('{:^30}'.format('BANCO CEV'))
print('=' * 30)
saque = int(input('Qual o valor você quer sacar? R$'))
cid = 50
total = saque
totalced = 0
while True:
    if total >= cid:
        total -= cid
        totalced += 1
    else:
        if totalced > 0:
            print(f'Total de {totalced} cédulas de R${cid}')
        if cid == 50:
            cid = 20
        elif cid == 20:
            cid = 10
        elif cid == 10:
            cid = 1
        totalced = 0
        if total == 0:
            break
print('=' * 30)
print('Volte sempre ao BANCO CEV! Tenha um bom dia!')

#ou

from math import trunc
print('=' * 30)
print('{:^30}'.format('BANCO CEV'))
print('=' * 30)
cin = 0
vinte = 0
dez = 0
um = 0
while True:
    saque = int(input('Que valor você quer sacar? R$'))
    cel = saque / 50
    cin = trunc(cel)
    if cin >= 1:
        print(f'Total de {cin} cédulas de R$50')
    rest = saque - (cin * 50)
    if rest != 0:
        while True:
            if rest % 20 == 0:
                cel2 = rest / 20
                vinte = trunc(cel2)
                if vinte >= 1:
                    print(f'Total de {vinte} cédulas de R$20')
                break
            if rest % 20 != 0:
                cel2 = rest / 20
                vinte = trunc(cel2)
                rest2 = rest - (vinte * 20)
                if rest2 != 0:
                    while True:
                        if rest2 % 10 == 0:
                            cel3 = rest2 / 10
                            dez = trunc(cel3)
                            if dez >= 1:
                                print(f'Total de {dez} cédulas de R$10')
                                break
                        if rest2 % 10 != 0:
                            cel3 = rest2 / 10
                            dez = trunc(cel3)
                            rest3 = rest2 - (dez * 10)
                            if dez >= 1:
                                print(f'Total de {dez} cédulas de R$10')
                                if rest3 == 0:
                                    break
                                if rest3 != 0:
                                    um = trunc(rest3)
                                    if um >= 1:
                                        print(f'Total de {um} cédulas de R$1')
                                        break
                                    if um == 0:
                                        break
                                break
                            break
                if rest2 == 0:
                    break
                break
            if rest == 0:
                break
    if cin == 0:
        break
    break
print('=' * 30)
print('Volte sempre ao BANCO CEV! Tenha um bom dia!')
