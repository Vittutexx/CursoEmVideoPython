import math
import random

aluno1 = input('Digite o nome do aluno: ')
aluno2 = input('Digite o nome do aluno: ')
aluno3 = input('Digite o nome do aluno: ')
aluno4 = input('Digite o nome do aluno: ')

sorteio = [aluno1, aluno2, aluno3, aluno4]

sortear = sorted(sorteio)

print("A ordem de apresentação será:\n{}".format(sortear))