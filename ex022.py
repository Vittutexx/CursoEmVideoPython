nome = input("Escreva seu nome: ")


nomeUpper = nome.upper()
nomeLower = nome.lower()
letrasnome = nome.split()

print("Seu nome em letras maiúsculas é: ",nomeUpper)
print("Seu nome em letras minúsculas é: ",nomeLower)
print("Seu nome tem ao todo: ",len(''.join(letrasnome)))
print("Seu primeiro nome é: {} e ele tem {}".format(letrasnome[0], len(letrasnome[0])))
