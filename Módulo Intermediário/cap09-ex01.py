from random import randint

Qtde = int(input('Digite a quantidade (max 50): '))

while Qtde > 50:
    print('Valor acima do permitido!')
    Qtde = int(input('Digite a quantidade (max 50): '))

conjunto = set()
while len(conjunto) < Qtde:
    conjunto.add(randint(1,50))

print(conjunto)
print(f'O conjunto tem {len(conjunto)} elemento(s).')
print('\nFim do programa.')
