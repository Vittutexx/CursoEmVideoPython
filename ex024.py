cidade = input("Escreva o nome da sua cidade: ")

cidadeUp = cidade.upper().strip()
listacidade = cidadeUp.split()

print("Sua cidade tem \"SANTO\" no começo: ",'SANTO' in listacidade[0])
