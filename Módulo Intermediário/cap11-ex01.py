arq = open('saida_er_11.1.txt', 'w')
A = int(input('Digite um inteiro: '))

while A != 0:
    arq.write(f'{A}\n')
    A = int(input('Digite um inteiro: '))
arq.close()

print('\nFim do programa.')