nota1 = float(input("Informe sua primeira nota: "))
nota2 = float(input("Informe sua segunda nota: "))

media = (nota1 + nota2) / 2

if media < 5.0:
    print("REPROVADO")
elif 5 <= media <= 6.9:
    print("RECUPERAÇÃO")
elif media >= 7.0:
    print("APROVADO")