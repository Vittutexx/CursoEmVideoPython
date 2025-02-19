import random

jokenpo = str(input("JO KEN...\n"))
listajo = ['pedra','papel','tesoura']
escolha = listajo[random.randrange(0, 2)]

print("PÔ")
if listajo == jokenpo:
    print("empate")
elif ((escolha == 'tesoura' and jokenpo == 'papel') or
      (escolha == 'pedra' and jokenpo == 'tesoura') or
      (escolha == 'papel' and jokenpo == 'pedra')):
    print("VENCI!!! SEU PERDEDOR HAHAHAHAHA")
else:
    print("Você venceu! Você é muito bom nisso.")
