soma = qtde = 0
A = int(input('Digite um valor: '))

while A != 0:
    soma += A
    qtde += 1
    A = int(input('Digite um valor: '))

print(f'Soma dos valores: {soma} - Quantidade: {qtde}')
print('Fim do programa.')