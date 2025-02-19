soma = 0
for x in range(1, 7):
    numero = int(input("Escolha um numero: "))

    if numero % 2 == 0:
        soma += numero
print("Total da soma dos numeros pares: ", soma)