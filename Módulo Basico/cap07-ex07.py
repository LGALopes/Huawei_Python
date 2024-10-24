from random import randint

Lst = []
Qtde = int(input('Digite a quantidade: '))

for i in range(Qtde):
    Lst.append(randint(1,20))
print('Lista gerada:')
print(Lst)

X = 1
while X > 0:
    X = int(input('Digite X: '))
    if X in Lst:
        print(f'    Há {Lst.count(X)} ocorrência(s) de {X} na lista.')
    else:
        print(f'    {X} não está na lista.')

print('Fim do programa.')
