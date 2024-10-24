lstValores = []
valor = int(input('Digite um inteiro: '))

while valor != 0:
    lstValores.append(valor)
    valor = int(input('Digite um inteiro: '))

print('\nResultado: \n')
print(lstValores)
print(f'A lista contém {len(lstValores)} elementos.')
print('\nFim do programa.')
