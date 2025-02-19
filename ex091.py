from operator import itemgetter
from random import randint
from time import sleep
jogadores = {'Jogador1':randint(1, 6),'Jogador2':randint(1, 6),
             'Jogador3':randint(1, 6),'Jogador4':randint(1, 6)}
print('Valores sorteados: ')
for c,v in jogadores.items():
    print(f'O {c} tirou {v} no dado  ')
    sleep(1)
listaV = list()
listaV = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
print('Ranking: ')
for i,v in enumerate(listaV):
    print(f'{i+1}º lugar: {v[0]} com o lado: {v[1]}')
    sleep(1)