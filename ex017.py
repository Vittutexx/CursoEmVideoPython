import math

c1 = int(input('Digite o valor do cateto oposto: '))
c2 = int(input('Digite o valor do cateto adjacente: '))

hipotenusa = pow(c1, 2) + pow(c2, 2)

print("O comprimento da hipotenusa é {:.2f}".format(hipotenusa))