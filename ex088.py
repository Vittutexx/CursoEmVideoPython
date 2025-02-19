from random import randint
from time import sleep
listaC = []
jogoT = []
cont = 0
print('-'*30)
print('{:^30}'.format('JOGA NA MEGASENA'))
print('-'*30)
palpite = int(input('Quantos jogos você quer que eu sorteie? '))
print(f'{("-="*3)} SORTEANDO {palpite} JOGOS {"-="*3}')
for x in range(1, palpite + 1):
    while True:
        num = randint(1, 60)
        if num not in jogoT:
            jogoT.append(num)
        if len(jogoT) == 6:
            break
    listaC.append(jogoT[:])
    jogoT.clear()
    listaC[cont].sort()
    print(f'jogo {x}: {listaC[cont]}')
    cont +=1
    sleep(0.5)
print(f'{("-="*4)} < BOA SORTE > {"-="*4}')
