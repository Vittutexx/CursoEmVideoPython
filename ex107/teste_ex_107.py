from ex107 import moeda

p = float(input('Digite o preço: '))

print(f'''
A metade de {p} é {moeda.metade(p)}
O dobro de {p} é {moeda.dobro(p)}
Aumentando em 10%, temos {moeda.aumentar(p, 10)}
Reduzindo em 13%, temos {moeda.diminuir(p,13)}
''')