valor = int(input("Informe o valor a ser sacado: R$"))
cedula = 50
total = valor
totalced= 0
while True:
    if cedula <= total:
        total -= cedula
        totalced += 1
    else:
        print(f'Total de {totalced} cédulas de R${cedula}')
        if cedula == 50:
            cedula = 20
            totalced = 0
        elif cedula == 20:
            cedula = 10
            totalced =  0
        elif cedula == 10:
            cedula = 1
            totalced = 0

        if total == 0:
            break
print('FIM')
