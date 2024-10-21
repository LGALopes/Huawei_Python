P = int(input('Digite o primeiro termo: '))
R = int(input('Digite a razão: '))
Q = int(input('Digite a quantidade de termos: '))
Termos = []
cont = 0

while cont < Q:
    Termos.append(P)
    P += R
    cont += 1

print('\nLista Resultante:')
print(Termos)
print('\n\nFim do programa.')
