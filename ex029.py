velocidade = int(input("Qual a velocidade que você está nesse momento? "))

limite = 80

multa =((velocidade - limite) * 7)


if velocidade > limite:
    print("Você ultrapassou o limite de 80km/h. Sua multa será no valor de R${}.".format(multa))

else:
    print("Mantenha-se abaixo do limite de 80km/h.")
