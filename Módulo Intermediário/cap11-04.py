Lst = []
arqEntr = open('entrada_er_11.4.txt', 'r')
linha = arqEntr.readline()

while linha != '':
    Lst.append(int(linha))
    linha = arqEntr.readline()
arqEntr.close()

print('Lista lida do arquivo')
print(Lst)
Soma = sum(Lst)
print(f'Soma dos valores = {Soma}')
Qtde = len(Lst)
print(f'Quantidade = {Qtde}')
print(f'Média dos valores = {Soma/Qtde}')
Minimo = min(Lst)
print(f'Mínimo dos valores = {Minimo}')
Maximo = max(Lst)
print(f'Mínimo dos valores = {Maximo}')

print('\nFim do programa')