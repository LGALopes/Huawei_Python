lstValores = []
valor = int(input('Digite um inteiro: '))

while valor != 0:
    if valor not in lstValores:
        lstValores.append(valor)
    else:
        print(f'    Erro. O valor {valor} já está na lista.')
    valor = int(input('Digite um inteiro: '))

print('\nResultado: \n')
print(lstValores)
print(f'A lista contém {len(lstValores)} elementos.')
print('\nFim do programa.')
