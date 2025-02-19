qtd = media = menor = maior = 0
continuar = 's'.upper()
while continuar != "N":
    numero = int(input("Escreva um numero inteiro: "))
    media += numero
    qtd += 1
    if media == numero:
        maior = numero
        menor = numero
    else:
        if numero > maior:
            maior = numero
        elif numero < menor:
            menor = numero
    continuar = str(input("Deseja continuar? [S/N] ")).strip().upper()[0]
print("Você digitou {} números e a média foi de {}".format(qtd, (media / qtd)))
print("O maior número digitado foi: {} e o menor digitado foi: {}".format(maior,menor))


