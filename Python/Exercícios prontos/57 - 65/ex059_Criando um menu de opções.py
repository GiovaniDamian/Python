from time import sleep
n1 = float(input('Primeiro valor: '))
n2 = float(input('Segundo valor: '))
opcao = 0
while opcao != 5:
    print('[ 1 ] Somar\n[ 2 ] Multiplicar\n[ 3 ] Maior\n[ 4 ] Novos números\n[ 5 ] Sair do programa')
    opcao = int(input('>>>>> Qual é a sua opção? '))
    if opcao == 1:
        soma = n1 + n2
        print('A soma entre {:.0f} + {:.0f} é {:.0f}'.format(n1, n2, soma))
    elif opcao == 2:
        mult = n1 * n2
        print('A multiplicação entre {:.0f} x {:.0f} é {:.0f}'.format(n1, n2, mult))
    elif opcao == 3:
        if n1 > n2:
            print('Entre {:.0f} e {:.0f} o maior valor é {:.0f}'.format(n1, n2, n1))
        elif n1 < n2:
            print('Entre {:.0f} e {:.0f} o maior valor é {:.0f}'.format(n1, n2, n2))
        else:
            print('Os valores {:.0f} e {:.0f} são iguais'.format(n1, n2))
    elif opcao == 4:
        print('Informe os números novamente:')
        n1 = float(input('Primeiro valor: '))
        n2 = float(input('Segundo valor: '))
    elif opcao == 5:
        print('Finalizando....')
        sleep(1)
        opcao = 5
    else:
        print('Opção inválida. Tente novamente')
        sleep(3)
    print('=-' * 20)
    sleep(3)
print('=-' * 20)
print('Fim do programa" Volte sempre!')
