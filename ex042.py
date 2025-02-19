r1 = int(input("Informe o valor do primeiro segmento: "))
r2 = int(input("Informe o valor do segundo segmento: "))
r3 = int(input("Informe o valor do terceiro segmento:  "))

if (r1 < r2+r3 and r2 < r1+r3 and r3 < r2+r1) and (r1 == r2 and r1 == r3):
    print("Triangulo equilátero")
elif(r1 < r2+r3 and r2 < r1+r3 and r3 < r2+r1) and (r1 == r2 != r3 or r1 == r3 != r2 or r3 == r2 != r1):
    print("Triangulo Isósceles")
elif (r1 < r2 + r3 and r2 < r1 + r3 and r3 < r2 + r1) and (r1 != r2 and r1 != r3 and r3 != r2):
    print("Triangulo Escaleno")
else:
    print("Não formam um triângulo")
