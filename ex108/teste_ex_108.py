from ex108 import moeda

p = float(input('Digite o preço: '))

print(f'''
A metade de {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}
O dobro de {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))}
Aumentando em 10%, temos {moeda.moeda(moeda.aumentar(p, 10))}
Reduzindo em 13%, temos {moeda.moeda(moeda.diminuir(p,13))}
teste temos {moeda.moeda(p)}
''')