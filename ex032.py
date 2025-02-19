
ano = int(input("Informe o ano em que você está: "))

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0  :
    print("Você está num ano bissexto")
else:
    print("Você está num ano normal.")