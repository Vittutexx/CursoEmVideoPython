from random import randint
from time import sleep
numeros = list()
def sorteia():
    print('Sorteando 5 valores da lista: ', end=' ')
    for x in range(0,6):
        numeros.append(randint(1,10))
        print(numeros[x], end = ' ')
        sleep(0.25)
    print()
def somaPar(num):
    par = []
    print(f'Somando os valores pares de {num}', end='')
    for x in num:
        if x % 2 == 0:
           par.append(x)
    print(f', temos {sum(par)}')
sorteia()
somaPar(numeros)