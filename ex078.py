lista = list()
maior = 0
menor = 0
for x in range(0, 5):
    lista.append(int(input(f"Digite um valor para a posição {x}: ")))
    if x == 0:
        maior = menor = lista[x]
    else:
        if maior < lista[x]:
            maior = lista[x]
        if menor > lista[x]:
            menor = lista[x]
print(f'Você digitou os valores: {lista}')
print(f'O maior valor digitado foi {maior} nas posições ', end= '')
for p,v in enumerate(lista):
    if v == maior:
        print(f'{p}...', end=' ')
print(f'\nO menor valor digitado foi {menor} nas posições ', end='')
for p,v in enumerate(lista):
    if v == menor:
        print(f'{p}...', end= ' ')