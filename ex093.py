jogador = dict()
jogador['Nome'] = str(input('Nome do Jogador: '))
jogador['Gols'] = []
partidas = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
for x in range(0,partidas):
    gols = int(input(f'Quantos gols na partida {x}? '))
    jogador['Gols'].append(gols)
jogador['Total'] = sum(jogador['Gols'])
print('=-'*40)
print(jogador)
print('=-'*40)
for c,v in jogador.items():
    print(f'O campo {c} tem o valor {v}')
print('=-'*40)
print(f'O jogador {jogador["Nome"]} jogou {partidas} partidas.')
for x in range(0, partidas):
    print(f'{" ":<3} => Na partida {x}, fez {jogador["Gols"][x]} gols.')
print(f'foi um total de {jogador["Total"]} gols.')