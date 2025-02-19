e = int(input("Escolha o numero da tabuada: "))

for x in range(1, 11):
    resultado = e * x
    print("{} X {} = {}".format(e, x, resultado))