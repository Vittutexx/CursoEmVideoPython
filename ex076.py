listagem = ('Lápis', 1.75,
            'Borracha', 2.00,
            'Caderno', 15.90,
            'Estojo', 25.00,
            'Transferidor', 4.20,
            'Compasso', 9.99,
            'Mochila', 120.32,
            'Canetas', 22.30,
            'Livro', 34.90)
print('_'*40)
print('{:^40}'.format('LISTA DE PRODUTOS'))
print('_'*40)
for x in range(0, len(listagem)):
    if x % 2 == 0:
        print(f'{listagem[x]:.<30}R$', end='')
    else:
        print(f'{listagem[x]:>8.2f}')
print('_'*40)


#CORRIGIDO