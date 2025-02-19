from math import factorial
escreva = int(input("Escreva um numero: "))
valor = escreva
print("{}! = {}".format(escreva, escreva), end='')
while escreva != 1:
    escreva -= 1
    print(" x {}".format(escreva), end='')
print(" = {}".format(factorial(valor)), end='')

