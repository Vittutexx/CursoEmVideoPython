import datetime

idade = int(input("Qual o ano de nascimento do atleta? "))

anoAtual = datetime.datetime.now().year

categoria = anoAtual - idade

if categoria <= 9:
    print("CATEGORIA MIRIM")
elif categoria <= 14:
    print("CATEGORIA INFANTIL")
elif categoria <= 19:
    print("CATEGORIA JUNIOR")
elif categoria <= 20:
    print("CATEGORIA SÊNIOR")
else:
    print("CATEGORIA MASTER")