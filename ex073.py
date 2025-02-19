brasileirao = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio',
               'Cruzeiro', 'Flamengo', 'Vasco', 'Chapecoense', 'Atlético', 'Botafogo',
               'Botafogo', 'Atlético-PR', 'Bahia', 'São Paulo', 'Fluminense', 'EC Vitória', 'Coritiba', 'Avaí', 'Ponte Preta', 'Atlético-GO')
chapeco = brasileirao.index('Chapecoense')
print('-='*40)
print(f'Lista de times do Brasileirão: {brasileirao}')
print('-='*40)
print(f'Os 5 primeiros são {brasileirao[0:6]}')
print('-='*40)
print(f'Os 4 últimos são {brasileirao[-4:]}')
print('-='*40)
print(f'Times em ordem alfabética: {sorted(brasileirao)}')
print('-='*40)
print(f'Chapecoense está na {chapeco + 1}ª posição')