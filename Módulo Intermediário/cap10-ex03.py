UF = {}
print('\t -- Leitura dos Dados --')

while True:
    sigla = input('Digite a sigla: ')
    if sigla == '':
        break
    elif sigla in UF:
        print('     A sigla já consta no cadastro!')
        continue
    estado = input('Digite o estado: ')
    capital = input('Digite a capital: ')
    pib = float(input('Digite o PIB: '))
    UF[sigla] = (estado, capital, pib)

print('     {:15} {:15} {:>10}'.format('Estado','Capital', 'PIB (R$ bi'))
for sigla, dados in UF.items():
    print('({}) {:15} {:15} {:10.1f}'.format(sigla, dados[0], dados[1], dados[2]))

print('\nFim do programa.')