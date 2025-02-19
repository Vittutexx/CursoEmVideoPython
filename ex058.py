import random
sorteado = random.randint(0, 10)
acumulo = 0
escolha = int(input("Estou pensando num número... Tente adivinhar qual é o numero entre 0 a 10\n"))
while escolha != sorteado:
    if escolha < sorteado:
        print("mais! Continue tentando.")
    else:
        print("Menos! Continue tentantndo")
    acumulo += 1
    escolha = int(input("Qual o seu palpite? \n"))
print('''Você acertou! Parabens!. 
A quantidade de palpites que foram errados foi de: {} '''.format(acumulo))