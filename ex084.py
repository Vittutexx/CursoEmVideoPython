
lista = []
listaPessoas = []
cont = 0
maior = 0
menor = 0
listaMe = []
listaMa = []
while True:
    lista.append(str(input('Nome: ')))
    lista.append(float(input('Peso: ')))
    if len(listaPessoas) == 0:
        maior = menor = lista[1]
    else:
        if lista[1] > maior:
            maior = lista[1]
        if lista[1] < menor:
            menor = lista[1]
    listaPessoas.append(lista[:])
    cont += 1
    lista.clear()
    continuar = str(input("Deseja continuar? [S/N] ")).strip().upper()[0]
    if 'N' in continuar:
        break
for x in listaPessoas:
    if x[1] == maior:
        listaMa.append(x[0])
for x in listaPessoas:
    if x[1] == menor:
        listaMe.append(x[0])

print(f'Total de pessoas cadastradas: {cont}')
print(f'Menor peso de {menor}KG. Lista das pessoas mais leves: {listaMe}',end=' ')
print(f'Maior peso de {maior}KG. Lista das pessoas mais pesadas: {listaMa}',end=' ')
