kmRodado = float(input("Informe a quantidade de kilometros rodados com o carro: "))
qtdDiasAlugados = int(input("Informe quantos dias que vc esteve alugando esse carro: "))

carro = 60 * qtdDiasAlugados
custoKmRodado = kmRodado * 0.15

precoPagar = carro + custoKmRodado

print("Você terá que pagar ao todo por R${}".format(precoPagar ))



