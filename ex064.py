numero = cont = soma = 0
numero = int(input("Digite um numero inteiro: "))
while numero != 999:
    cont += 1
    soma += numero
    numero = int(input("Digite um numero inteiro: "))
print("Total de números digitados: {}".format(cont))
print("Soma total entre os numeros digitados: {}".format(soma))
