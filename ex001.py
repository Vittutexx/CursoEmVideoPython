from random import randint


print("Olá mundo!")



valores = (randint(0, 10),randint(0, 10),randint(0, 10),randint(0, 10),randint(0, 10))
ordenar = sorted(valores)
maior = ordenar[-1]
menor = ordenar[0]
print(f'Sorteei os valores {valores}')
print(f'O maior valor é {maior}')
print(f'O menor valor é {menor}')


