numero = int(input("Digite um numero: "))
cont = 0
for x in range(1, numero + 1):
    print(x, end= ' ')
    if numero % x == 0:
        cont += 1
print("\nContagem de números divisíveis: {}".format(cont))
if cont > 2:
    print("O {} não é um numero primo. É um numero inteiro.".format(numero))
else:
    print("O {} é um numero primo!!".format(numero))



#CORRIGIDO