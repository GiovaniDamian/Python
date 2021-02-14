from random import randint
comp = (randint(1, 10), randint(1, 10), randint(1, 10),
        randint(1, 10), randint(1, 10))
print('Os valores sorteados forma: ', end='')
for n in comp:
    print(f'{n} ', end='')
print(f'\nO maior valor sorteado foi {max(comp)}')
print(f'O menor valor sorteado foi {min(comp)}')

#ou

comp = (randint(1, 10), randint(1, 10), randint(1, 10),
        randint(1, 10), randint(1, 10))
ordem = sorted(comp)
print(f'Os valores sorteados foram : {comp[0]} {comp[1]} {comp[2]} {comp[3]} {comp[4]}')
print(f'O maior valor sorteado foi {ordem[-1]}')
print(f'O menor valor sorteado foi {ordem[0]}')
