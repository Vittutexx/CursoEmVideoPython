num1 = int(input("Escreva um número: "))
num2 = int(input("Escreva outro número: "))

if num1 > num2:
    print("O primeiro número é maior".format(num1, num2))
elif num2 > num1:
    print("O segundo numero é maior".format(num2, num1))
else:
    print("Os numeros são iguais".format(num1, num2))
