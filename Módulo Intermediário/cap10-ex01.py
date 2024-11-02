produtos = {}
print('\t-- Leitura dos Dados --')
cod = input('   Digite o Código: ')

while cod != '':
    preco = float(input('   Digite o Preço: '))
    produtos[cod] = preco
    cod = input('   Digite o Código: ')
print('\t-- Fim da Leitura dos Dados --\n')

print('Preço dos Produtos:')
for cod in produtos.keys():
    print(f'    Produto {cod} custa R$ {produtos[cod]:7.2f}')

print('\nFim do programa.')