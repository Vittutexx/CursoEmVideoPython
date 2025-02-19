lista = [[],[]]
for x in range(1,8):
    valor = int(input(f"Informe  o {x}o valor: "))
    if valor % 2 == 0:
        lista[0].append(valor)
    else:
        lista[1].append(valor)
lista[0].sort()
lista[1].sort()
print(f'Lista de pares: {lista[0]}')
print(f'Lista de ímpares: {lista[1]}')