palavra = str(input("Escreva uma frase: ")).strip().upper()
listap = palavra.split(' ')
listajun = ''.join(listap)
listano = ''
for x in range(len(listajun) -1, -1, -1):
    listano += listajun[x]
print(listano, end=' ')
if listano == listajun:
    print("É um palíndromo")
else:
    print("É uma frase normal")








