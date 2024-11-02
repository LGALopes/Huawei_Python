Lst = []
X = float(input('Digite um real: '))
while X != 0:
    Lst.append(f'{X:.3f}\n')
    X = float(input('Digite um real: '))

arq = open('saida_er_11.3.txt', 'w')
arq.writelines(Lst)
arq.close()

print('\nFim do programa.')