from ex109 import moeda

p = float(input('Digite o preço: '))

print(f'''
A metade de {moeda.moeda(p)} é {moeda.metade(p, True)}
O dobro de {moeda.moeda(p)} é {moeda.dobro(p, True)}
Aumentando em 10%, temos {moeda.aumentar(p, 10, True)}
Reduzindo em 13%, temos {moeda.diminuir(p,13, True)}
teste temos {moeda.moeda(p)}
''')