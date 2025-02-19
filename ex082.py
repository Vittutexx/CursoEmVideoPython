lista = []
listaPar = []
listaImpar = []
while True:
    valor = int(input("Digite um valor: "))
    lista.append(valor)
    continuar = str(input("Deseja continuar? [S/N] ")).strip().upper()[0]
    if 'N' in continuar:
        break
print(f'A lista completa é {lista}')
for pos, x in enumerate(lista):
    if x % 2 == 0:
        listaPar.append(lista[pos])
    if x % 2 != 0:
        listaImpar.append(lista[pos])
print(f'A lista de pares é {listaPar}')
print(f'A lista de ímpares é {listaImpar}')

