from random import randint
def CarregaLista():
    L = []
    for i in range(10):
        L.append((randint(1,1000)))
    return L

print('Início do programa')
valores = CarregaLista()
print(f'Lista Gerada >> {valores}')

print('\nFim do programa')