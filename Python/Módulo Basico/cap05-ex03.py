P = int(input('Digite o primeiro termo: '))
R = int(input('Digite a razão: '))
cont = 1

while cont <= 10:
    print(P, end=', ')
    P += R
    cont += 1

print('\n\nFim do programa.')
