produtos = {}
print('\t-- Leitura dos Dados --')

while True:
    cod = input('   Digite o Código: ')
    if cod == '':
        break
    elif cod in produtos:
        print(f'    O código {cod} já existe!')
        continue
    preco = float(input('   Digite o Preço: '))
    produtos[cod] = preco
print('\t-- Fim da Leitura dos Dados --\n')

print('Preço dos Produtos:')
for cod in produtos.keys():
    print(f'    Produto {cod} custa R$ {produtos[cod]:7.2f}')

print('\nFim do programa.')