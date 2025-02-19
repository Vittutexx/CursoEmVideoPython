distancia = int(input("Qual será a distancia da viagem?"))

valorNormal = 0.50 * distancia

valorMaior = distancia * 0.45

if distancia <= 200:
    print("O valor da passagem será de R${:.2f}.".format(valorNormal))
else:
    print("O valor da passagem será de R${:.2f}.".format(valorMaior))