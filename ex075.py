v1 = v2 = v3 = v4 = 0
pares = 0
while True:
    v1 = int(input("Escreva um valor: "))
    v2 = int(input("Escreva um valor: "))
    v3 = int(input("Escreva um valor: "))
    v4 = int(input("Escreva um valor: "))
    valores = (v1,v2,v3,v4)
    qtdVezes9 = valores.count(9)
    print(f"Você digitou os valores {valores}")
    print(f"O numero 9 apareceu {qtdVezes9} vezes.")
    if 3 in valores:
        posicao3 = valores.index(3)
        print(f"O primeiro valor 3 foi digitado na {posicao3 + 1}ª posição ")
    else:
        print("O valor 3 não foi digitado em nenhuma posição")
    print("Os valores pares digitados foram ", end='')
    for x in valores:
        if x % 2 == 0:
            print(f'{x} ', end='')
    break
