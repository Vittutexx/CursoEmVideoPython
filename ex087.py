matriz = [[0,0,0],[0,0,0],[0,0,0]]
soma = somaTerceiraC = 0
maiorv = []
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite um valor para [{l},{c}]: '))
        if matriz[l][c] % 2 == 0:
            soma += matriz[l][c]
        if matriz[l] == matriz[1]:
            maiorv.append(matriz[l][c])
        if matriz[l][c] == matriz[l][2]:
            somaTerceiraC += matriz[l][c]
for l in range(0,3):
   for c in range(0,3):
       print(f'[{matriz[l][c]:^5}]', end='')
   print()
print(f'A soma dos valores pares é {soma}')
print(f'A soma dos valores  da terceira coluna é {somaTerceiraC}')
maiorv.sort()
print(f'O maior valor da segunda linha é {maiorv[-1]}')


