frase = input("Escreva uma frase: ")

print('Vezes que a letra A estve na frase',frase.strip().upper().count('A'))
print('Primeira posição em que a letra A esteve na frase: ',frase.strip().upper().find('A')+1)
print('Ultima posição em a letra A esteve na frase: ',frase.strip().upper().rfind('A')+1)


