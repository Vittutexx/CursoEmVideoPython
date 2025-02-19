menor = 0
maior = 0
for x in range(1, 6):
    valor = int(input("Qual é o seu peso? "))
    if x == 1:
        maior = valor
        menor = valor
    else:
        if valor > maior:
            maior = valor
        if valor < menor:
            menor = valor
print("o maior valor foi de {}".format(maior))
print("o menor valor foi de {}".format(menor))
#CORRIGIDO