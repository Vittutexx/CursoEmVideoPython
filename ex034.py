sal = float(input("Digite o seu salario R$"))

calculoMaior = sal + (sal * 0.15)
calculoMenor = sal + (sal * 0.10)
if sal > 1250:
    print("Seu salário aumentou para {}.".format(calculoMenor))

if sal <= 1250:
    print("Seu salário aumentou para {}".format(calculoMaior))
