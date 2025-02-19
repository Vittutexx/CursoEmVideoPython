r1 = int(input("Informe o valor da reta 1 "))
r2 = int(input("Informe o valor da reta 2 "))
r3 = int(input("Informe o valor da reta  "))

if r1 < r2+r3 and r2 < r1+r3 and r3 < r2+r1:
    print("Forma um triangulo")
else:
    print("Não forma um triangulo")

