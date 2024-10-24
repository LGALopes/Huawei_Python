N = int(input('Digite a quantidade: '))
LNeg = []
LPos = []

for i in range(N):
    X = int(input(f'Elemento {i} >>> '))
    if X >= 0:
        LPos.append(X)
    else:
        LNeg.append(X)

print(f'\nLista de Negativos: {LNeg}, contém {len(LNeg)} elementos.')
print(f'\nLista de Positivos: {LPos}, contém {len(LPos)} elementos.')
print('\n\nFim do programa.')
