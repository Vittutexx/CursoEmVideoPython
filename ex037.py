numero = int(input("Escolha um numero: "))
escolha = int(input("Escolha entre as opções a seguir a base de conversão:\n1 - Binário\n2 - Octal\n3- Hexadecimal\n"))


if escolha == 1:
    numerob = bin(numero)
    print("O valor de {} para binário é: {}".format(numero, numerob[2:]))
elif escolha == 2:
    numerooc = oct(numero)
    print("O valor de {} para octal é: {}".format(numero, numerooc[2:]))
elif escolha == 3:
    numerohex = hex(numero)
    print("O valor de {} para hexadecimal é: {}".format(numero, numerohex[2:]))
else:
    print("Opção inválida. Tente novamente")