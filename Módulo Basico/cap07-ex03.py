N = int(input('Digite a quantidade: '))
L = []

for i in range(N):
    x = float(input(f'Elemento {i}: '))
    L.append(x)

print('\nResultado:')
for valor in L:
    print(f'{valor:.2f}')

print('\nFim do Programa.')
