d = float(input('Uma distância em metros: '))
print('A medida de {}m corresponde a \n{}Km\n{}hm\n{:.1f}dam\n{:.0f}dm\n{:.0f}cm\n{:.0f}mm'.format(d, d*0.001, d*0.01, d*0.1, d*10, d*100, d*1000))
