soma = cont = 0
while True:
    numero = int(input("Informe um numero (999 para parar): "))
    if numero == 999:
        break
    soma += numero
    cont += 1
print(f'''A soma total dos numeros foi: {soma}. A quantidade de numeros digitados foi de {cont}''')