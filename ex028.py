
import random

sorteio = [1,2,3,4,5]
sorteado = random.choice(sorteio)

numeroEscolhido = int(input("Estou pensando num numero... \nAdivinhe o número que estou pensando: "))

if numeroEscolhido == sorteado:
    print("Você é muito bom nisso! Acertou.")
else:
    print("Você errou feio, o numero certo era {}.".format(sorteado))