import math

graus = float(input("Informe os graus: "))

seno = math.sin(math.radians(graus))
cosseno = math.cos(math.radians(graus))
tangente = math.tan(math.radians(graus))

print("SENO: {}\nCOSSENO: {}\nTANGENTE: {}".format(seno, cosseno,tangente))